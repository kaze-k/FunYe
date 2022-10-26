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
    data_index = Reactive(-1)
    cursor = CURSOR

    def __init__(self, **kwargs: Any) -> None:
        super().__init__()
        self.layout_size = 3

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
