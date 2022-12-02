x = input().strip()
x = x[1: -2]
if ('[' not in x):
    print("Cannot Unpack")
else:
    x = x.split(',')
    print(len(x))


# [[1, 2], 'a', "Hello"]

# [1, 2, 3]
