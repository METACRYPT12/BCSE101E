# Write a program to print n numbers in ascending order

a = []
n = int(input("How many numbers do you want to enter: "))
i = 0
print("Enter the numbers:")
while (i < n):
    a.append(int(input()))
    i = i+1
i = 0
while (i < n):
    j = i+1
    while (j < n):
        if (a[i] > a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        j = j+1
    i = i+1
print(a)
