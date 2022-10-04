# Write a program to exchange two integer numbers

a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
print("Before Swap:")
print("a is", a, "\nb is", b)
temp = a
a = b
b = temp
print("After Swap:")
print("a is", a, "\nb is", b)
