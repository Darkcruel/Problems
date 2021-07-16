# link : https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    row = [0]* len(container)
    col = [0]* len(container)

    for i in range(len(container)):
        for j in range(len(container)):
            row[i] += container[i][j]
            col[i] += container[j][i]
            
    if sorted(row) == sorted(col):
        return 'Possible'
    else:
        return 'Impossible'

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result)
