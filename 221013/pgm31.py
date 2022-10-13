# Convert the upper characters available in the string into lowercase

s = input("Enter a String: ")
i = 0
ch = ''
while s[i:]:
    temp = ord(s[i])
    if temp > 64 and temp < 90:
        ch = ch + chr(temp + 32)
    else:
        ch = ch + chr(temp)
    i = i + 1
print("The String in Lowercase is:", ch)

"""
ch=s.lower()
print("The String in Lowercase is:", ch)
"""
