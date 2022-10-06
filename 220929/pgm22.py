# Write a program to print the Fibonacci Series

n = int(input("How many numbers do you want to print(n>2): "))
if (n < 2):
    print("Enter a number greater than 2!")
else:
    a, b = 0, 1
    i = 2
    print(a, "\t", b, "\t", end="")
    while (i < n):

        temp = a+b
        a = b
        b = temp

        """
        Alternatively...

        b = a+b
        a = b-a
        print(b,"\t",end="")
        """

        print(temp, "\t", end="")
        i = i+1
