# link : https://www.hackerrank.com/challenges/sock-merchant/problem

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    answer = 0
    count = dict()
    for i in ar:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    
    res = sorted(count.items())
    for i in res:
        if i[1]>1:
            answer += (i[1]//2)
    return answer