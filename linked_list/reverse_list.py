#!/bin/python3

import os
import sys


#
# Complete the reverseArray function below.
#
def reverseArray(a):
    l = []
    for i in range(len(a) - 1, -1, -1):
        l.append(a[i])
    return l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
