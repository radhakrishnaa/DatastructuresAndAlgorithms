l1 = [1, 3, 5, 8, 90, 100]
l2 = [3, 4, 10]

def merge(l1, l2):
    short = l1 if len(l1) <= len(l2) else l2
    long = l1 if len(l1) >= len(l2) else l2
    l3 = []
    i = 0
    j = 0
    while i < len(short) and j < len(long):
        if short[i] <= long[j]:
            l3.append(short[i])
            i += 1
        else:
            l3.append(long[j])
            j += 1
    while j < len(long):
        l3.append(long[j])
        j += 1
    return l3


l3 = merge(l1, l2)
print l3
