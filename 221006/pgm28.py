# Write a program to display lowercase and uppercase letters and digits in a String

lower = 0
upper = 0
digits = 0
s = input("Enter a String: ")
for i in s:
    if (i >= 'a' and i <= 'z'):
        lower = lower + 1
    elif (i >= 'A' and i <= 'Z'):
        upper = upper + 1
    elif (i >= '0' and i <= '9'):
        digits = digits + 1
print("There are", lower, "lowercase letters and",
      upper, "uppercase letters and", digits, "digits in \"", s, "\"")
