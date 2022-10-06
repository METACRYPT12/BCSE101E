# Write a program reverse a given number

n = int(input("Enter a number: "))
rev = 0
temp = n
while (temp != 0):
    r = temp % 10
    rev = (rev*10)+(r)
    temp = int(temp/10)
print("Reverse of", n, "is", rev)
