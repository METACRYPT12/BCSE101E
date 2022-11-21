# Create a module to find biggest among 2, 3, and 10 numbers

import biggest2
import biggest3
import biggest10

n = int(input("How many numbers do you want to Enter(2, 3, or 10): "))
a = []
if (n == 2):
    for i in range(n):
        a.append(int(input()))
        print("Biggest number: ", biggest2.big(a))
elif (n == 3):
    for i in range(n):
        a.append(int(input()))
    print("Biggest number: ", biggest3.big(a))
elif (n == 10):
    for i in range(n):
        a.append(int(input()))
    print("Biggest number: ", biggest10.big(a))
