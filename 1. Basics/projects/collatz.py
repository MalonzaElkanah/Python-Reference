def collatz(number):
    if number % 2 == 0:
        return number//2
    else:
        return (3*number)+1


num = int
print("Lets Generate a COLLATZ pattern")
try:
    num = int(input("ENTER AN INTEGER NUMBER:"))

except ValueError:
    print("Enter An Interger Number PLease: ")
    num = int(input("ENTER AN INTEGER NUMBER:"))

print(num, end=" ", sep=",")
while num != 1:
    num = collatz(num)
    print(num, end=" ", sep=",")
