# Find the factorial of a given number

n = int(input("Enter a number: "))
fact = 1
temp = n
while (temp > 1):
    fact = fact*temp
    temp = temp-1
print("Factorial of", n, "is", fact)
