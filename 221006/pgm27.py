# Write a program to display lowercase and uppercase letters in a String

lower = 0
upper = 0
s = input("Enter a String: ")
for i in s:
    if (i >= 'a' and i <= 'z'):
        lower = lower + 1
    elif (i >= 'A' and i <= 'Z'):
        upper = upper + 1
print("There are", lower, "lowercase letters and",
      upper, "uppercase letters in \"", s, "\"")
