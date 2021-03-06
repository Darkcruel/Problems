#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    result = [0,0] 
    for i in range(len(topic)-1):
        for j in range(i+1 , len(topic)):
            sum_pair = str(int(topic[i])+int(topic[j]))
            count = sum_pair.count('1')+sum_pair.count('2')
            if count > result[0]:
                result[0] = count
                result[1] = 1
            elif count == result[0]:
                result[1] +=1

    return result

if __name__ == '__main__':
   

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)
    print(result[0] , result[1])

    
