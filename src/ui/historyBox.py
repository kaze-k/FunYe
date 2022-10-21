from __future__ import annotations

from typing import TYPE_CHECKING, Tuple

from rich import box
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from textual.widget import Widget

from config import (
    HISTORYBOX_TITLE,
    HISTORYBOX_INIT_TEXT_AND_STYLE,
    HISTORYBOX_INIT_BORDER_STYLE,
    HISTORYBOX_UPDATE_BORDER_STYLE
)

if TYPE_CHECKING:
    from rich.console import RenderableType


class HistoryBox(Widget, can_focus=False):
    renderable: RenderableType = Panel(
        Align.center(
            HISTORYBOX_INIT_TEXT_AND_STYLE,
            vertical="middle"
        ),
        title=HISTORYBOX_TITLE,
        border_style=HISTORYBOX_INIT_BORDER_STYLE,
        box=box.ROUNDED
    )

    def render(self) -> RenderableType:
        """组件渲染"""
        return self.renderable

    async def update(self, text: Text) -> None:
        """更新组件，重新渲染"""
        self.renderable = Panel(
            text,
            title=HISTORYBOX_TITLE,
            border_style=HISTORYBOX_UPDATE_BORDER_STYLE,
            box=box.ROUNDED
        )
        self.refresh()
