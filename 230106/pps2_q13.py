data = open("230106\diabetes.csv", "r")
lines = 0
nullVal = 0
for line in data:
    for value in line.strip().split(","):
        if (value == "0"):
            nullVal = nullVal + 1
    lines = lines + 1
print(lines)
print(nullVal)
data.seek(0)
newfile = open("230106\File.csv", "r+")
newfile.writelines(data)
newfile.seek(0)
print(newfile.read())
data.close()
newfile.close()
