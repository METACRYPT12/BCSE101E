# Find the numbers which are divisible by 6 from 1 to 100

n = 1
while (n < 101):
    if ((n % 6) == 0):
        print(n, "is divisible by 6.")
        n = n+1
