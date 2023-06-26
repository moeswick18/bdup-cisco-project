import os

def find_dir(path, dir):
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            if dirname == dir:
                dirname = os.path.join(dirpath, dirname)
                print(dirname)

find_dir(input('path='), input('dir='))
