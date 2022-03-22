def generategrid(x, y):
    grid = []
    for i in range(x):
        grid2 = []
        for j in range(y):
            grid2.append(str(i)+str(j))

        grid.append(grid2)
    return grid


def printgrid(gd):
    for val in gd:
        print(val)


print("Enter the length of a 2D grid")
x = int(input("X: "))
y = int(input("Y: "))
grid = generategrid(x, y)
printgrid(grid)
