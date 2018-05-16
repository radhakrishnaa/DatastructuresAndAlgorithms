def selectionSort(alist):
    for i in range(0, len(alist)-1):
        max_in = 0
        for j in range(1, len(alist)-i):
            if(alist[max_in]<alist[j]):
                max_in = j
        print(i, max_in, j)
        if (max_in != j):
            temp = alist[max_in]
            alist[max_in] = alist[j]
            alist[j] = temp



alist = [54,26,93,77,31,44,55,20,77]
selectionSort(alist)
print(alist)