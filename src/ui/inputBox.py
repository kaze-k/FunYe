from __future__ import annotations

from typing import TYPE_CHECKING, Any

from textual_inputs import TextInput
from textual import events
from rich import box
from datetime import datetime
from rich.panel import Panel
from rich.text import Text
from textual.reactive import Reactive

from config import(
    CURSOR, INPUTBOX_TITLE,
    INPUTBOX_BORDER_STYLE,
    INPUTBOX_TEXT_STYLE
)

if TYPE_CHECKING:
    from rich.console import RenderableType


class InputBox(TextInput):
    height = 8
    data_index = Reactive(-1)
    cursor = CURSOR

    def __init__(self, **kwargs: Any) -> None:
        super().__init__()
        self.layout_size = 10

    @property
    def _visible_width(self) -> int:
        """InputBox的可见宽度"""
        width, _ = self.size
        overflow_width = 33
        width = width * self.height - overflow_width

        return width

    def _cursor_enter(self) -> None:
        """按回车键后改变光标和文本（换行达到InputBox的最大高度将无法换行）"""
        newline_number = len(self.value.split("\n"))
        if newline_number != self.height:
            self.value += "\n"
            self._cursor_position += 1
            self._update_offset_right()

        if self._cursor_position != len(self.value):
            temp = list(self.value)
            index = self._cursor_position -1
            temp.insert(index, "\n")
            self.value = "".join(temp)

    def _cursor_tab(self) -> None:
        """按tab键后改变光标和文本"""
        self.value += "\t"
        self._cursor_position += 1
        self._update_offset_right()

        if self._cursor_position != len(self.value):
            temp = list(self.value)
            index = self._cursor_position -1
            temp.insert(index, "\t")
            self.value = "".join(temp)

    def _key_backspace(self) -> None:
        """删空InputBox中的内容就重新初始化历史索引"""
        super()._key_backspace()
        if self.value == "":
            self.data_index = -1

    def _key_delete(self) -> None:
        """删空InputBox中的内容就重新初始化历史索引"""
        super()._key_delete()
        if self.value == "":
            self.data_index = -1

    async def on_key(self, event: events.Key) -> None:
        """新增enter键和tab(ctrl+i)键的控制"""
        if event.key == "ctrl+i":
            self._cursor_tab()

        if event.key == "enter":
            self._cursor_enter()

    def render(self) -> RenderableType:
        """组件渲染"""
        segments = self._render_text_with_cursor()
        text = Text.assemble(
            *segments,
            style=INPUTBOX_TEXT_STYLE,
            justify="left"
        )

        return Panel(
            text,
            title=INPUTBOX_TITLE,
            title_align="left",
            border_style=INPUTBOX_BORDER_STYLE,
            box=box.ROUNDED
        )

    async def clear_input(self) -> None:
        """清空InputBox中的内容"""
        self.value = ""
        self._cursor_position = 0
        self._text_offset = 0
        self.data_index = -1
