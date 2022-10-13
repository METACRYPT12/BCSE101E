# Convert the lower characters available in the string into uppercase

s = input("Enter a String: ")
i = 0
ch = ''
while s[i:]:
    temp = ord(s[i])
    if temp > 96 and temp < 123:
        ch = ch + chr(temp - 32)
    else:
        ch = ch + chr(temp)
    i = i + 1
print("The String in Uppercase is:", ch)

"""
ch=s.upper()
print("The String in Uppercase is:", ch)
"""
