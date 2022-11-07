import os
import sys
import getopt


helper = """
用法: python devtools.py [选项]

短选项:
    -h            : 查看帮助
    -I            : 安装项目中所需依赖
    -i dev        : 安装项目中开发环境依赖
    -i all        : 安装项目中全部的依赖(项目所需依赖和开发环境依赖)
    -c            : 清理pip缓存(需pip版本>=20.1)
    -C            : 编译二进制文件
    -l            : 检查项目代码是否符合标准
    -t            : 检查项目代码是否有类型错误
    -r            : 运行项目
    -R            : 移除项目中安装的所有依赖
    -p            : 安装pre-commit

长选项:
    --help        : 查看帮助
    --install     : 安装项目中所需依赖
    --install-dev : 安装项目中开发环境依赖
    --install-all : 安装项目中全部的依赖(项目所需依赖和开发环境依赖)
    --clean       : 清理pip缓存(需pip版本>=20.1)
    --compile     : 编译二进制文件
    --lint        : 检查项目代码是否符合标准
    --type        : 检查s项目代码是否有类型错误
    --run         : 运行项目
    --remove      : 移除项目中安装的所有依赖
    --pre-commit  : 安装pre-commit
"""
error = "\n错误: 选项错误\n"
tips = error + helper


def command(nt, posix):
    if os.name == "nt":
        tips = "» " + nt
        print(tips)
        os.system(nt)
    elif os.name == "posix":
        tips = "» " + posix
        print(tips)
        os.system(posix)
    else:
        print("? 未知系统")
        sys.exit(3)

def install():
    print("\n» 正在安装项目中所需依赖...")
    command(
        r".\.venv\Scripts\pip install -e .",
        "./.venv/bin/pip install -e ."
    )

def install_dev():
    print("\n» 正在安装项目中开发环境依赖...")
    command(
        r".\.venv\Scripts\pip install -e .[dev]",
        "./.venv/bin/pip install -e .[dev]"
    )

def clean():
    print("\n» 正在清理pip缓存...")
    command(
        r".\.venv\Scripts\pip cache purge",
        "./.venv/bin/pip cache purge"
    )

def compiler():
    print("\n» 正在编译二进制文件...")
    command(
        r".\.venv\Scripts\pyinstaller -F .\app.py -n FunYe -i .\img\icon.ico",
        "./.venv/bin/pyinstaller -F ./app.py -n FunYe"
    )

def lint():
    print("\n» 正在检查项目代码是否符合标准...")
    command(
        r".\.venv\Scripts\flake8 src && .\.venv\Scripts\flake8 app.py",
        "./.venv/bin/flake8 src && ./.venv/bin/flake8 app.py"
    )

def types():
    print("\n» 正在检查项目代码是否有类型错误...")
    command(
        r".\.venv\Scripts\mypy src && .\.venv\Scripts\mypy app.py",
        "./.venv/bin/mypy src && ./.venv/bin/mypy app.py"
    )

def run():
    print("\n» 正在运行项目...")
    command(
        r".\.venv\Scripts\python .\app.py",
        "./.venv/bin/python ./app.py"
    )

def remove():
    print("\n» 正在移除项目中安装的所有依赖...")
    command(
        r".\.venv\Scripts\pip uninstall -r requirements.txt -y",
        "./.venv/bin/pip uninstall -r requirements.txt -y"
    )

def pre_commit():
    print("\n» 正在安装pre-commit...")
    command(
        r".\.venv\Scripts\pre-commit install",
        "./.venv/bin/pre-commit install"
    )

def main(argv):
    try:
        opts, args = getopt.getopt(
            argv,
            "hIi:cCltrRp",
            [
                "help",
                "install",
                "install-dev",
                "install-all",
                "clean",
                "compile",
                "lint",
                "type",
                "remove",
                "pre-commit"
            ]
        )
    except getopt.GetoptError:
        print(tips)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(helper)
        elif opt in ("-I", "--install"):
            install()
        elif opt == "-i" and arg == "dev" or opt == "--install-dev":
            install_dev()
        elif opt == "-i" and arg == "all" or opt == "--install-all":
            install()
            install_dev()
        elif opt in ("-c", "--clean"):
            clean()
        elif opt in ("-C", "--compile"):
            compiler()
        elif opt in ("-l", "--lint"):
            lint()
        elif opt in ("-t", "--type"):
            types()
        elif opt in ("-R", "--remove"):
            remove()
        elif opt in ("-r", "--run"):
            run()
        elif opt in ("-p", "--pre-commit"):
            pre_commit()
        else:
            print(tips)
            sys.exit(2)
    if not opts:
        print(tips)
        sys.exit(2)


if __name__ == "__main__":
    path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
    os.chdir(path)
    main(sys.argv[1:])
