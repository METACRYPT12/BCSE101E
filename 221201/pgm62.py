# 1 [a-z]
# 1 [A-Z]
# 1 [0-9]
# 1 #@$
import re
x = tuple(input().split(','))
final = []
for i in x:
    if (len(i) > 5 and len(i) < 13):
        test_res = [0, 0, 0, 0]
        test_res[0] = 0 if (re.search("[a-z]", i) == None) else 1
        test_res[1] = 0 if (re.search("[A-Z]", i) == None) else 1
        test_res[2] = 0 if (re.search("\d", i) == None) else 1
        if ('@' in i or '#' in i or '$' in i):
            test_res[3] = 1
        if (0 not in test_res):
            final.append(i)
if (len(final) == 0):
    print("invalid")
else:
    for i in final:
        print(i)
