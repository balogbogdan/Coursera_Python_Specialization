# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fh = open('mbox.txt')
x = 0
z = 0
count = 0
for line in fh:

    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        x = line.rstrip("\n")
        print(count, x)

        y = line.find("0.")
        z = z + (float)(line[20:26])
z = z/count



print("Average spam confidence: ", z)
