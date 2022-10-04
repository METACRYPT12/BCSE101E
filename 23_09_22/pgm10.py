# Find if the given number is Armstrong number or not

n = int(input("Enter a Number: "))
sum = 0
temp = n
while (temp != 0):
    r = temp % 10
    sum = sum+pow(r, 3)
    temp = int(temp/10)
if (n == sum):
    print(n, "is an Armstrong Number.")
else:
    print(n, "is not an Armstrong Number.")
