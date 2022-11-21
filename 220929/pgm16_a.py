# Find the biggest among 10 numbers

a = []
i = 0
print(("Enter 10 numbers: "))
while (i < 10):
    n = int(input())
    a.append(n)
    i = i+1
print(a)
big = a[0]
i = 1
while (i < 10):
    if (big < n):
        big = n
    i = i+1
print("Biggest among the entered numbers is:", big)
