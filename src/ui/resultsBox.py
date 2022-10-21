from __future__ import annotations

from typing import TYPE_CHECKING

from rich import box
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from textual.widget import Widget

from config.style import (
    RESULTSBOX_TITLE,
    RESULTSBOX_INIT_TEXT_AND_STYLE,
    RESULTSBOX_INIT_BORDER_STYLE,
    RESULTSBOX_UPDATE_BORDER_STYLE
)

if TYPE_CHECKING:
    from rich.console import RenderableType


class ResultsBox(Widget, can_focus=False):
    renderable = Panel(
        Align.center(
            RESULTSBOX_INIT_TEXT_AND_STYLE,
            vertical="middle"
        ),
        title=RESULTSBOX_TITLE,
        border_style=RESULTSBOX_INIT_BORDER_STYLE,
        box=box.ROUNDED
    )

    def render(self) -> RenderableType:
        """组件渲染"""
        return self.renderable

    async def update(self, text: Text) -> None:
        """更新组件，重新渲染"""
        self.renderable = Panel(
            Align.center(text, vertical="middle"),
            title="💡结果",
            border_style=RESULTSBOX_UPDATE_BORDER_STYLE,
            box=box.ROUNDED
        )
        self.refresh()
