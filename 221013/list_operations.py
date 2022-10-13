my_list = ['p', 'r', 'o', 'b', 'e']
# first item
print(my_list[0])
# third item
print(my_list[2])
# fifth item
print(my_list[4])

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]
# Nested indexing
print(n_list[0][1])

print(n_list[1][3])

# Negative indexing in lists
# last item
print(my_list[-1])
# fifth last item
print(my_list[-5])

# concatenating and repeating lists
odd = [1, 3, 5]
# concatenation
print(odd+[9, 7, 5])
# repeatation
print(["re"]*3)

# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1, 3)

print(odd)

odd[2:2] = [5, 7]

print(odd)

# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
# delete one item
del my_list[2]

print(my_list)
# delete multiple items
del my_list[1:5]
print(my_list)

# List comprehension
pow2 = [2**x for x in range(10)]
print(pow2)
