fhandle = open("doc.txt")

for line in fhandle:
    x = line.rstrip("\n")
    print(x)

