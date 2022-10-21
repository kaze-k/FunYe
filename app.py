from __future__ import annotations

from typing import TYPE_CHECKING, List, Any
from datetime import datetime
from io import StringIO

from textual.app import App
from rich.text import TextType, Text

from src.ui import HistoryBox, InputBox, ResultsBox, Header
from src.script import Translation, Handler
from config import (
    TIME_SYMBOL,
    HISTORY_TIME_STYLE,
    HISTORY_DATA_STYLE,
    RESULTS_ORIGINAL_STYLE,
    RESULTS_TRANSLATION_STYLE,
    RESULTS_ERROR_STYLE,
    TITLE
)


class FunYe(App):
    time_io: _io.StringIO = StringIO()
    data_io: _io.StringIO = StringIO()
    dataList: List[str] = []

    async def on_load(self) -> None:
        """按键绑定"""
        await self.bind("escape", "quit", show=False)
        await self.bind("f1", "submit", show=False)
        await self.bind("up", "before_history", show=False)
        await self.bind("down", "after_history", show=False)
        await self.bind("ctrl+l", "clear_input", show=False)

    async def on_mount(self) -> None:
        """应用挂载后的布局以及立即聚焦InputBox"""
        self.header = Header()
        self.history = HistoryBox()
        self.results = ResultsBox()
        self.input = InputBox()

        await self.view.dock(self.header, edge="top")
        await self.view.dock(self.history, edge="left", size=40)
        await self.view.dock(self.results, self.input, edge="top")

        await self.input.focus()

    async def action_before_history(self) -> None:
        """获取上一个输入记录"""
        dataList = self.dataList
        if self.input.data_index < len(dataList) - 1:
            self.input.data_index += 1
            self.input.value = dataList[self.input.data_index]
            self.input._cursor_position = len(self.input.value)
        if self.input.value == "":
            self.input.data_index = -1

    async def action_after_history(self) -> None:
        """获取历史中下一次输入记录"""
        dataList = self.dataList
        if self.input.data_index < len(dataList) - 1:
            self.input.data_index -= 1
            self.input.value = dataList[self.input.data_index]
            self.input._cursor_position = len(self.input.value)
        if abs(self.input.data_index) == len(dataList):
            self.input.data_index = 0

    async def action_clear_input(self) -> None:
        """情况InputBox中的内容"""
        await self.input.clear_input()

    async def action_submit(self) -> None:
        """
        提交输入的内容后清空InputBox中的内容并更新HistoryBox和ResultsBox，
        如果没有实质性的内容则只清空不提交
        """
        value = self.input.value

        if value != "" and not value.isspace():
            history_text = await self.handle_history_data()
            results_text = await self.handle_results_data()
            await self.history.update(history_text)
            await self.results.update(results_text)

        await self.input.clear_input()

    async def action_quit(self) -> None:
        """关闭开启的内存并关闭应用"""
        self.time_io.close()
        self.data_io.close()
        await self.shutdown()

    async def handle_history_data(self) -> Text:
        """将从InputBox中获取的数据存入内存中，并进行格式化处理"""
        empty = ""

        formatted_time = TIME_SYMBOL + datetime.now().time().strftime("%X") + "\r"
        formatted_data = self.input.value + "\r"

        self.time_io.write(formatted_time)
        self.data_io.write(formatted_data)

        meta_time = self.time_io.getvalue()
        meta_data = self.data_io.getvalue()

        time_list = meta_time.split("\r")
        data_list = meta_data.split("\r")

        time_list.reverse()
        data_list.reverse()
        del time_list[0]
        del data_list[0]

        history_data = Handler.formatter(
            time_list,
            data_list,
            HISTORY_TIME_STYLE,
            HISTORY_DATA_STYLE,
            "\n\n"
        )

        data_list.append(empty)
        self.dataList = data_list

        return history_data

    async def handle_results_data(self) -> Text:
        """将翻译结果渲染到ResultsBox中，并进行格式化处理"""
        value = self.input.value
        original, translation = Translation(value).run()

        if translation:
            results_data = Handler.formatter(
                original,
                translation,
                RESULTS_ORIGINAL_STYLE,
                RESULTS_TRANSLATION_STYLE
            )
        else:
            results_data = Text(original, style=RESULTS_ERROR_STYLE)

        return results_data


if __name__ == "__main__":
    FunYe.run(title=TITLE)
