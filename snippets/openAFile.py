path = "./text/LittlePrince.txt"

# Use this
with open(path, 'r', encoding="utf-8") as f:
    print(f.readline())

# Don't use this
f = open(path, 'r')
print(f.readline())
f.close()
