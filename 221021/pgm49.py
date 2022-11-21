"""
1 2 3 4 
1 2 3
1 2
1
"""

rows = 4
for i in range(rows, 0, -1):
    for j in range(i):
        print(j+1, end=" ")
    print()
