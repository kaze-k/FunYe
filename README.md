# FunYe

![screenshot](./img/show.gif)

**FunYe**是一个基于[Textual](https://github.com/Textualize/textual)框架的TUI翻译应用

## 使用

Windows

`program`目录下的FunYe.exe是Windows上的可执行文件，下载到本地，到Powershell中切换到文件所在目录下，输入以下命令即可使用。（实测在windows自带的终端模拟器无法完整渲染，最好使用Windows Terminal)

```Powershell
./FunYe.exe
```

Linux

`program`目录下的FunYe是Linux上的可执行文件，下载到本地，到终端中切换到文件所在目录下，输入以下命令即可使用。

```bash
source ./FunYe
```

快捷键

- `F1` 提交翻译内容
- `up` 上一个输入记录
- `down` 下一个输入记录
- `ESC` 退出程序
- `ctrl+l` 清空输入框中的内容

## 编译

Windows

```powershell
./bin/build.bat
```

Linux

```bash
source ./bin/build.sh
```

## 配置颜色样式
`config/style.py`中可以进行颜色的调整，修改后重新构建一下即可。

## 技术
- [Textual](https://github.com/Textualize/textual)是一个python的TUI框架

- [Rich](https://github.com/Textualize/rich)是一个 Python 库，可以为您在终端中提供富文本和精美格式

- [textual-inputs](https://github.com/sirfuzzalot/textual-inputs)是一个基于Textual的输入小组件

- [网易有道翻译](https://fanyi.youdao.com/)