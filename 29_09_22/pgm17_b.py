# Find the biggest among n numbers

size = int(input("How many numbers do you want to Enter: "))
big = int(input())
i = 1
while (i < size):
    n = int(input())
    if (big < n):
        b = n
    i = i+1
print("Biggest among the entered numbers:", big)
