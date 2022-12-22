# +2 -0.5


key = ['A', 'B', 'B', 'A', 'C']  # list to store correct keys
n = int(input())  # Storing the number of candidates
C = []  # Temporary list to store Candidate marks
marks = []  # Final list that stores Marks
for i in range(n):
    C.append(input().split())
    marks.append(0.0)  # Initialising marks[]
    for j in range(5):
        if (C[i][j] == key[j]):  # Matching Candidate answers with keys
            marks[i] = marks[i] + 2.0
        elif (C[i][j] == 'X'):
            continue
        else:
            marks[i] = marks[i] - 0.5

c_order = marks.copy()  # copied marks to a new list to maintain Candidate order
print(c_order)
marks.sort(reverse=True)  # sorting marks in descending order

print("Rank\t", "Candidate\t", "Marks")
i = 0
j = 1  # Variable initialised to indicate Rank
if (len(list(set(marks))) == len(marks)):  # checking if elements are unique
    while (len(marks) != i):
        print(j, end="\t")  # printing Rank
        print("C{0}".format(c_order.index(marks[i]) + 1),
              end="\t\t")  # Printing Candidate
        print(marks[i])  # Printing Candidate`s Marks
        i = i + 1
        j = j + 1

else:
    dup = set()  # Initialising new set to store same marks
    for k in range(len(marks)):
        for l in range(len(marks)):
            # Checking if 2 or more Candidates have Same Marks
            if marks[k] == marks[l] and k != l:
                dup.add(marks[k])  # Adding duplicates to Set
    while (len(marks) > i + 1):
        if (marks[i] in dup):  # Checking if scored mark exist in dup set
            pos = []  # List to store position of duplicates
            pos.append(i)  # Storing first identified duplicate
            for k in range(i + 1, len(marks)):  # Iterating through marks[] to find duplicates
                if (marks[i] == marks[k]):
                    pos.append(k)
            print(j, end="\t")  # Printing Rank
            for k in pos:  # iterating through pos[] to print Candidates with same marks
                if (marks[k] in dup and marks[k] in c_order):
                    print("C{0} ".format(c_order.index(marks[k]) + 1), end="")
                    # updating already printed mark to defunct values
                    tempPurgeVar = marks[k]
                    c_order[c_order.index(marks[k])] = -50
            print(end="\t\t")
            dup.remove(tempPurgeVar)
            print(marks[i])  # Printing Candidate`s Marks
            i = i + 1
            j = j + 1
        else:
            print(j, end="\t")  # Printing Rank
            print("C{0} ".format(c_order.index(marks[i]) + 1), end="\t\t")
            # updating already printed mark to defunct values
            c_order[c_order.index(marks[i])] = -50
            print(marks[i])  # Printing Candidate`s Marks
        i = i + 1
        j = j + 1
