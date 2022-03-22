def generatelist():
    print("Enter a number of value to a list. \n ... Enter Nothing to mark end of the list")
    k = 1
    list1 = []
    while True:
        j = input("ENTER VALUE " + str(k) + ": ")
        if j == "":
            break
        else:
            list1.append(j)
        k += 1
    return list1


def degeneratelist(lists):
    print("This is my list is", sep=",", end=" ")
    for val in range(len(lists)):
        if val == (len(lists)-1):
            print(lists[val], end=".")
        elif val == (len(lists) - 2):
            print(lists[val], end=" and ")
        else:
            print(lists[val], end=", ")


mylist = generatelist()
print(mylist)
degeneratelist(mylist)
