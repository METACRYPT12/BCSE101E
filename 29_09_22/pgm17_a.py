# Find the biggest among n numbers

a = []
i = 0
size = int(input("How many numbers do you want to Enter: "))
while (i < size):
    n = int(input())
    a.append(n)
    i = i+1
print(a)
big = a[0]
i = 1
while (i < size):
    if (big < n):
        big = n
    i = i+1
print("Biggest among the entered numbers is:", big)
