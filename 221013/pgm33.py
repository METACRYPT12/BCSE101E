# Write a program to reverse a given String

s = input("Enter a String: ")
news = ""
for i in s:
    news = i + news
print("\"", s, "\"in reverse is\"", news, "\"")


"""
newS =s [::-1]
print("\"", s, "\"in reverse is\"", newS, "\"")
"""
