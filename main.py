import os


def get_files(path: str) -> bytearray or bool:
    if os.path.isdir(path):
        found = []
        for root, dirs, files in os.walk(path, topdown=True):
            for name in files:
                path = os.path.join(root, name)
                found.append(path)
        return found
    else:
        return False


def read_file(path: str) -> bytes or bool:
    if os.path.isfile(path):
        file_ = open(path, "r")
        data = file_.read()
        file_.close()
        return data
    else:
        return False


cats = get_files(input("Enter folder name: "))
if cats:
    for file in cats:
        data = read_file(file)
        print(data)
else:
    print("Folder is not exists")
