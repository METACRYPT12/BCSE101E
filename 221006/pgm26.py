# Write a program to display lowercase letters in a String

count = 0
s = input("Enter a String: ")
for i in s:
    if (i >= 'a' and i <= 'z'):
        count = count + 1
print("There are", count, "lowercase letters in \"", s, "\"")
