largest = None
smallest = None
lst = list()

while True:
    num = input("Enter a number: ")

    try:
        lst.append(int(num))
    except:
        if num == "done":
            break
        else:
            print("Invalid input")
            continue

for x in lst:
    if largest is None:
        largest = x
    elif x > largest:
        largest = x

    if smallest is None:
        smallest = x
    elif x < smallest:
        smallest = x

print("Maximum is ", largest)
print("Minimum is ", smallest)