import os


def clear(file_path):
    files = os.listdir(file_path)
    if ".venv" in files:
        files.remove(".venv")
    for fd in files:
        cur_path = os.path.join(file_path, fd)
        if os.path.isdir(cur_path):
            if fd == "__pycache__":
                files = os.listdir(cur_path)
                for fd in files:
                    file_path = os.path.join(cur_path, fd)
                    os.remove(file_path)
                    print("删除 %s" % file_path)
                os.removedirs(cur_path)
                print("删除 %s" % cur_path)
            else:
                clear(cur_path)

def main():
    if os.name == "nt":
        clear(".\\")
    elif os.name == "posix":
        clear("./")
    else:
        print("未知系统：无法清理")

if __name__ == "__main__":
    main()
