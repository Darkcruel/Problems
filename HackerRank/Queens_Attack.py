import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    if(n==1):
        return 0
    result = 0
    move_q = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,1),(-1,-1),(1,-1)]
    
    for move in move_q:
        pos = (r_q+move[0] , c_q+move[1])
        while(1<=pos[0]<=n and 1<=pos[1]<=n and [pos[0] , pos[1]] not in obstacles):
            result +=1
            pos = (pos[0]+move[0] , pos[1]+move[1])
               
    return result
                
if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)