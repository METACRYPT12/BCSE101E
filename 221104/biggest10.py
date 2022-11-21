def big(l):
    big = l[0]
    i = 1
    while (i < len(l)):
        if (big < l[i]):
            big = l[i]
        i = i+1
    return big
