from os import listdir
from os.path import isfile, join


path = "./text"

# The variable files will contain all files in the folder "path"
files = [f for f in listdir(path) if isfile(join(path, f))]

for file in files:
    with open(join(path, file), 'r', encoding="utf-8") as f:
        print(f.readline())
