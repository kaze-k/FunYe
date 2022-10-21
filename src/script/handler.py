from typing import Any
from datetime import datetime

from rich.text import Text
from rich.text import TextType
from rich.style import Style


class Handler:
    def formatter(list1: Any, list2: Any, style1: Style, style2: Style, char: str="\n") -> Text:
        """给不同数据添加不同的样式"""
        data = Text("")
        for i in range(len(list1)):
            data1 = Text(list1[i], style=style1)
            data2 = Text(list2[i], style=style2)
            data += data1 + "\n" + data2 + char

        return data