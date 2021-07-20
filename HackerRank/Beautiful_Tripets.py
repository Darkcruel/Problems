# link : https://www.hackerrank.com/challenges/beautiful-triplets/problem

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    result = 0
    for idx in range(1 , len(arr)-1):
        upper = arr[idx+1:].count(arr[idx]+d)
        lower = arr[0:idx].count(arr[idx]-d)
        
        result += (upper*lower)
    return result  