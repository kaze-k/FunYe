"""
该文件为样式的配置文件

Style()：一个样式类
具体参数：https://github.com/Textualize/rich/blob/62de8e4caf2f4f588df07052e3af428662945ed5/rich/style.py#L31

Args:
    color(Union[Color, str], 可选)：文本颜色
    bold(bool, 可选)：加粗字体
    italic(bool, 可选)：斜体
    dim(bool, 可选)：暗浅色，开启后文本闪烁无非使用
    underline(bool, 可选)：下划线
    blink(bool, 可选)：文本闪烁


Text()：一个文本类
具体参数：https://github.com/Textualize/rich/blob/62de8e4caf2f4f588df07052e3af428662945ed5/rich/text.py#L105
"""

from rich.style import Style
from rich.text import Text


# Header
HEADER_LEFT_TEXT_STYLE = Style(
    color="#b3ee39",
    italic=True,
    bold=True
)

HEADER_RIGHT_TEXT_STYLE = Style(
    color="#ffffff",
    italic=False,
    bold=True
)


# InputBox
CURSOR = (
    "|",
    Style(
        color="#ffffff",
        blink=True,
        bold=True,
    )
)

INPUTBOX_TITLE = Text(
    "📝输入",
    Style(
        bold=False,
        italic=False,
        dim=False,
        blink=False
    )
)

INPUTBOX_TEXT_STYLE = Style(
    color="#b6abf5",
    bold=False,
    italic=False,
    dim=False,
    underline=False,
    blink=False
)

INPUTBOX_BORDER_STYLE = Style(
    color="#b6abf5"
)


# HistoryBox
HISTORYBOX_TITLE = Text(
    "📑历史",
    Style(
        bold=False,
        italic=False,
        dim=False,
        blink=False
    )
)

HISTORYBOX_INIT_TEXT_AND_STYLE = Text(
    "暂无记录",
    Style(
        color="#78d3f2",
        bold=True,
        italic=False,
        dim=False,
        blink=False
    )
)

HISTORYBOX_INIT_BORDER_STYLE = Style(
    color="#78d3f2"
)

HISTORYBOX_UPDATE_BORDER_STYLE = Style(
    color="#78d3f2"
)


# ResultsBox
RESULTSBOX_TITLE = Text(
    "💡结果",
    Style(
        bold=False,
        italic=False,
        dim=False,
        blink=False
    )
)

RESULTSBOX_INIT_TEXT_AND_STYLE = Text(
    "暂无记录",
    Style(
        color="#fad314",
        bold=True,
        italic=False,
        dim=False,
        blink=False
    )
)

RESULTSBOX_INIT_BORDER_STYLE = Style(
    color="#fca39f"
)

RESULTSBOX_UPDATE_BORDER_STYLE = Style(
    color="#fca39f"
)


# App
TIME_SYMBOL = "• "

HISTORY_TIME_STYLE = Style(
    color="#ffffff",
    bold=False,
    italic=True,
    dim=False,
    blink=False
)

HISTORY_DATA_STYLE = Style(
    color="#78d3f2",
    bold=False,
    italic=False,
    dim=False,
    blink=False
)

RESULTS_ORIGINAL_STYLE = Style(
    color="#b6abf5",
    bold=False,
    italic=True,
    dim=False,
    blink=False,
    underline=True
)

RESULTS_TRANSLATION_STYLE = Style(
    color="#78d3f2",
    bold=True,
    italic=False,
    dim=False,
    blink=False,
    underline=False
)

TITLE = "FunYe"
