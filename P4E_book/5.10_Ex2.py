largest = None
smallest = None
num_list = []

while True:
    num = input("Enter a number: ")
    try:
        num = int (num)
        num_list.append(num)
    except:
        if num != 'done':
            print("Invalid input")
    largest = max(num_list)
    smallest = min(num_list)

    if num == "done" :
        break

#print(num_list)

print("Maximum is", largest)
print("Minimum is", smallest)