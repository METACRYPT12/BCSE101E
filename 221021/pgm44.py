"""
1       2       3       4
2       2       3       4
3       3       3       4
4       4       4       4
"""

for i in range(4):
    for j in range(4):
        if (j < i):
            print(i+1, end="\t")
        else:
            print(j+1, end="\t")
    print()
