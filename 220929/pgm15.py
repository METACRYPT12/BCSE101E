# Find the biggest among three numbers

a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
c = int(input("Enter third Number: "))
if (a > b & a > c):
    print(a, "is greatest.")
elif (b > c):
    print(b, "is greatest.")
else:
    print(c, "is greatest.")
