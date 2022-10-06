# Read and display 3x3 matrix

print("Enter the elements for a 3x3 matrix.")

a = []

for i in range(0, 3):
    v = []
    for j in range(0, 3):
        n = int(input())
        v.append(n)
    a.append(v)
    print("")

print("The Matrix is: ")

for i in range(0, 3):
    for j in range(0, 3):
        print(a[i][j], end="\t")
    print("")
