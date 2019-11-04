def merge_sort(l):
    if len(l) > 1:
        middle = len(l)/2
        lft = l[:middle]
        rgt = l[middle:]

        merge_sort(lft)
        merge_sort(rgt)

        i = j = k = 0

        while i< len(lft) and j< len(rgt):
            if lft[i] < rgt[j]:
                l[k] = lft[i]
                k += 1
                i += 1
            else:
                l[k] = rgt[j]
                k += 1
                j += 1

        while i < len(lft):
            l[k] = lft[i]
            k += 1
            i += 1

        while j < len(rgt):
            l[k] = rgt[j]
            k += 1
            j += 1

# a = [10, 2, 5, 3, 6]
merge_sort([10, 2, 5, 3, 6])
# print a
