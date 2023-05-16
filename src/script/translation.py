from typing import Any, List, Tuple, Dict
import urllib.request as request
import urllib.parse as parse
import urllib
import json

from config.base import (
    URL,
    HEAD,
    LOADING_TEXT,
    ERROR_TEXT
)


class Translation:
    url: str = URL
    head: Dict[str, str] = HEAD

    def __init__(self, value: str) -> None:
        self.arg = {
            "i": value,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web"
        }

    def handle_request(self) -> Any:
        """处理请求"""
        meta = parse.urlencode(self.arg).encode("utf-8")
        send_request = request.Request(self.url, meta, self.head)
        accept_response = LOADING_TEXT
        accept_response = request.urlopen(send_request)

        return accept_response

    def handle_response(self) -> List[List[Dict[str, str]]]:
        """处理响应"""
        accept_response = self.handle_request()
        read_response = accept_response.read().decode("utf-8")
        meta = json.loads(read_response)
        accept_response.close()
        translateResult = meta["translateResult"]

        return translateResult

    def handle_data(self) -> Tuple[List[str], List[str]]:
        """处理响应得到的数据"""
        translateResult = self.handle_response()
        original_list = []
        translation_list = []
        for i in range(len(translateResult)):
            original = translateResult[i]
            for i in range(len(original)):
                original_text = original[i]["src"]
                original_list.append(original_text)
                translation_text = original[i]["tgt"]
                translation_list.append(translation_text)

        return original_list, translation_list

    def run(self) -> Any:
        """返回已处理的数据，并处理错误"""
        try:
            return self.handle_data()
        except urllib.error.URLError:
            data = ERROR_TEXT
            return data, None
