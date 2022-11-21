"""
    1
   232
  34543
 4567654
567898765
"""

rows = 5
x = 0
for i in range(rows+1):
    for j in range(rows, i, -1):
        print(" ", end="")
    for k in range(i):
        print(k+x, end="")
    for l in range(i - 1, 0, -1):
        print(l+x-1, end="")
    x = x + 1
    print()
