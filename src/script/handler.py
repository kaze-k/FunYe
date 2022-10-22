from typing import Any, List, Optional
from datetime import datetime

from rich.text import TextType, Text
from rich.style import Style


class Handler:
    def formatter(
        style1: Style,
        style2: Style,
        list1: Any,
        list2: Any,
        list3: Optional[List] = None,
        style3: Optional[Style] = None,
        char: str = "\n"
    ) -> Text:
        """给不同数据添加不同的样式"""
        data = Text("")
        for i in range(len(list1)):
            data1 = Text(list1[i], style=style1)
            data2 = Text(list2[i], style=style2)
            if list3:
                data3 = Text(list3[i], style=style3)
                data += data1 + "\n" + data2 + "\n" + data3 + char
            else:
                data += data1 + "\n" + data2 + char

        return data
