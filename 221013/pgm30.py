# count the number of characters available in a string

count = 0
s = input("Enter a String: ")
for i in s:
    count = count + 1
print("The String is", count, "characters long.")

'''
count = len(s)
print("The String is",count,"characters long.")
'''
