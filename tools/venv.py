import os
import sys


def venv_path(path):
    if os.name == "nt":
        env = os.path.join(path, ".venv", "Scripts")
    elif os.name == "posix":
        env = os.path.join(path, ".venv", "bin")
    else:
        print("? 未知系统")
        sys.exit(1)
    return env

def check_venv(path):
    PATH = os.getenv("PATH")
    env = venv_path(path)
    if not env in PATH:
        print("! 请进入虚拟环境")
        if os.name == "nt":
            print("» 请使用以下命令进入虚拟环境")
            print(r"» .\.venv\Scripts\activate")
            sys.exit(2)
        elif os.name == "posix":
            print("» 请使用以下命令进入虚拟环境")
            print("» source ./.venv/bin/activate")
            sys.exit(2)

def create_venv(path):
    files = os.listdir(path)
    if not ".venv" in files:
        print("» 正在创建虚拟环境...")
        os.system("python -m venv .venv")
        check_venv(path)
    else:
        print("» 虚拟环境已创建")
        check_venv(path)

def main():
    path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
    create_venv(path)


if __name__ == "__main__":
    main()
