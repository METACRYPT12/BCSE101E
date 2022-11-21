rows = 5
x = 1
for i in range(rows+1):
    for j in range(rows, i, -1):
        print(" ", end='')
    for k in range((2*i) - 1):
        print("*", end="")
    print()
