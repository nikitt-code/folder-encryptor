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


cats = get_files(input("Enter folder name: "))
if cats:
    print(cats)
else:
    print("Folder is not exists")
