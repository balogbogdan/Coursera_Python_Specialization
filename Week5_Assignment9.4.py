#name = input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)

handle = open("mbox.txt")

emails = list()
for line in handle:
    lst = list()
    line = line.rstrip()
    if line.startswith("From "):
        for i in line.split():
            lst.append(i)
        emails.append(lst[5])

#print(emails)
hours = list()
for i in emails:
    line = i.split(":")
    hours.append(line[0])


counts = dict()
for hour in hours:
    counts[hour] = counts.get(hour,0) + 1
#print(counts)

for (k,v) in sorted(counts.items()):
    print (k,v)



