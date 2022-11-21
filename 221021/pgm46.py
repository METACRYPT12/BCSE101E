"""
1 
1 2
1 2 3
1 2 3 4
"""

rows = 4
for i in range(rows):
    for j in range(0, i+1):
        print(j+1, end=" ")
    print()
