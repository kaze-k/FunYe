from rich.table import Table
from rich.style import Style
from textual import events
from textual.widgets import Header

from config import (
    HEADER_LEFT_TEXT_STYLE,
    HEADER_RIGHT_TEXT_STYLE
)


class Header(Header):
    def __init__(self) -> None:
        super().__init__()
        self.tall = False
        self.style = None

    def render(self) -> Table:
        header_table = Table.grid(padding=(0, 1), pad_edge=True, expand=True)
        header_table.add_column(
            "title", justify="left", style=HEADER_LEFT_TEXT_STYLE
        )
        header_table.add_column(
            "clock", justify="right", style=HEADER_RIGHT_TEXT_STYLE
        )
        header_table.add_row(
            self.full_title, self.get_clock() if self.clock else ""
        )
        return header_table

    async def on_click(self, event: events.Click) -> None:
        return await super().on_click(event)
