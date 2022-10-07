# Write a program to display the Multiplication of two 3x3 matrices

print("Enter the elements for first 3x3 matrix.")

a1 = []
a2 = []
prod = []

for i in range(0, 3):
    v = []
    for j in range(0, 3):
        n = int(input())
        v.append(n)
    a1.append(v)
    print("")

print("Enter the elements for second 3x3 matrix.")

a2 = []

for i in range(0, 3):
    v = []
    for j in range(0, 3):
        n = int(input())
        v.append(n)
    a2.append(v)
    print("")

print("The first Matrix is: ")

for i in range(0, 3):
    for j in range(0, 3):
        print(a1[i][j], end="\t")
    print("")

print("The second Matrix is: ")

for i in range(0, 3):
    for j in range(0, 3):
        print(a2[i][j], end="\t")
    print("")

for i in range(0, 3):
    v = []
    for j in range(0, 3):
        sum1 = 0
        for k in range(0, 3):
            sum1 = sum1+a1[i][k]*a2[k][j]
        v.append(sum1)
    prod.append(v)

print("The product of the Matrices is: ")

for i in range(0, 3):
    for j in range(0, 3):
        print(prod[i][j], end="\t")
    print("")
