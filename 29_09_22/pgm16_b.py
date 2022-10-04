# Find the biggest among three numbers

print(("Enter 10 numbers: "))
big = int(input())
i = 1
while (i < 10):
    n = int(input())
    if (big < n):
        big = n
    i = i+1
print("Biggest among the entered numbers:", big)
