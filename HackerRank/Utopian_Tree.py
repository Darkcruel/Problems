# link : https://www.hackerrank.com/challenges/utopian-tree/problem

def utopianTree(n):
    # Write your code here
    result = [1]*(n+1)
    result[0] = 1
    for i in range(1,n+1):
        if (i%2==0):
            result[i] = result[i-1]+1
        else:
            result[i] = 2*result[i-1]
    return result[n]