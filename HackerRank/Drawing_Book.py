# link : https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    # Write your code here
    if(p==1 or p==n):
        return 0
    else:
        result = min(p//2 , n//2-p//2)
    return result