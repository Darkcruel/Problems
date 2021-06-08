# link : https://www.hackerrank.com/challenges/counting-valleys/problem

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    result = 0
    pos = 0
    for i in range(steps):
        if path[i] == 'U':
            pos +=1
        else:
            if pos==0:
                result +=1
            pos -=1
    return result