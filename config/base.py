"""
该文件是网易有道翻译接口的配置文件
"""


# 网易有道翻译的接口
URL = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

# 请求头参数
HEAD = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31'
}

# 报错提示
ERROR_TEXT = "网络不佳，请检查网络！"
