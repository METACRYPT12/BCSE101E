# Find the number of zeros in a given number

n = int(input("Enter a number: "))
temp = n
count = 0
while (temp > 0):
    r = temp % 10
    if (r == 0):
        count = count+1
    temp = int(temp/10)
print("Number of zeros in", n, "is:", count)
