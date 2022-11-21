def big(l):
    if (l[0] > l[1] & l[0] > l[2]):
        return l[0]
    elif (l[1] > l[2]):
        return l[1]
    else:
        return l[2]
