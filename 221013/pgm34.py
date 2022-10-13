# Find the second biggest among n numbers

l = []
big = 0
big2 = 0
n = int(input("How many numbers do you want to enter(At least 2): "))
i = 0
if n > 1:
    print("Enter", n, "Numbers.")
    while i < n:
        l.append(int(input()))
        i = i + 1
    if (l[1] > l[0]):
        big2 = l[0]
        big = l[1]
    else:
        big2 = l[1]
        big = l[0]
    for i in range(2, len(l)):
        if (big < l[i]):
            big2 = big
            big = l[i]
        elif (big2 < l[i]):
            big2 = l[i]
    print(l)
    print("The second biggest number is:", big2)
else:
    print("Enter a number greater than 1!")
