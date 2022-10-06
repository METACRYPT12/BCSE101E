# Find the sum of digits of a given number

sum = 0
n = int(input("Enter the number: "))
temp = n
while (temp != 0):
    r = temp % 10
    sum = sum+(r)
    temp = int(temp/10)
print("Sum of digits of", n, "is", sum)
