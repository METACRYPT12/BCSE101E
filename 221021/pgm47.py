"""
A      
B B     
C C C 
D D D D
"""
rows = 4
ascii_val = ord('A')
for i in range(rows):
    for j in range(0, i+1):
        print(chr(ascii_val+i), end=" ")
    print()
