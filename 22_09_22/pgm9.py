# Write a program to find it the number is Palindrome or not

n = int(input("Enter a number: "))
temp = n
rev = 0
while (temp != 0):
    r = temp % 10
    rev = (rev*10)+(r)
    temp = int(temp/10)
print(rev)
if (n == rev):
    print(n, "is a Palindrome.")
else:
    print(n, "is not a Palindrome.")
