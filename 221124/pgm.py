# +2 -0.5


a = ['A', 'B', 'B', 'A', 'C']
n = int(input())
C = []
marks = []
for i in range(n):
    C.append(input())
    marks.append(0.0)
    for j in range(5):
        if (C[i][j] == a[j]):
            marks[i] = marks[i] + 2.0
        elif (C[i][j] == 'X'):
            continue
        else:
            marks[i] = marks[i] - 0.5

l = []
for i in range(len(marks)):
    l.append(i+1)

rank = marks.copy()
print(rank)
marks.sort()
# print(rank)
# print(marks)

marks = marks[::-1]

print("Rank\t", "Candidate\t", "Marks")
i = 0
j = 1
if (len(list(set(marks))) == len(marks)):
    while (len(marks) != i):
        print(j, end="\t")
        print("C", rank.key(marks[i]) + 1, end="\t\t")
        print(marks[i])
        i = i + 1
        j = j + 1

else:
    dup = []
    for k in range(len(marks)):
        for l in range(len(marks)):
            if marks[k] == marks[l] and k != l:
                dup.append(marks[k])
    dup = list(set(dup))
    while (len(marks) != i):
        if (marks[i] in dup):
            pos = []
            pos.append(i)
            for k in range(i + 1, len(marks)):
                if (marks[i] == marks[k]):
                    pos.append(k)
            print(j, end="\t")
            for k in pos:
                if (marks[k] in dup and marks[k] in rank):
                    print("C", rank.index(marks[k]) + 1, end="")
                    rank[rank.index(marks[k])] = -50
            print(end="\t\t")
            print(marks[i])
        else:
            print(j, end="\t")
            print("C", rank.index(marks[i]) + 1, end="\t\t")
            rank[rank.index(marks[i])] = -50
            print(marks[i])
        i = i + 1
        j = j + 1
