import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    # Write your code here
    res = 0
    for n in range(len(ar)):
        res = res + ar[n]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()