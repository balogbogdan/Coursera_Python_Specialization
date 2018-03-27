fname = input("Enter file name: ")
fh = open("fisier.txt", 'r')
for line in fh:
    line = line.rstrip("\n>")
    line = line.lstrip()
    print (line.upper())