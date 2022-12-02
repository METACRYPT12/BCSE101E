import re
n = 0
a = []
while (n < 2):
    lst = input().split()
    a.append(dict(zip(lst[0], lst[1])))
    n = n + 1
print(a)
for i in range(len(a)):
    a[i] = dict(zip(a[i], map(int, a[i].values())))
print(a)
name = list(list(x.keys())[0] for x in a)
age = list((list(x.values())[0] for x in a))
print(name)
print(age)
agedup = re.match({2, 7}, age)
print(agedup)
