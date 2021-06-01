# link : https://www.hackerrank.com/challenges/the-birthday-bar/problem

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m

def birthday(s, d, m):
    # Write your code here
    result = 0
    for i in range(len(s)-m+1):
        total = 0
        for j in range(i,i+m):
            total += s[j]
        print(total)
        if(total == d):
            result +=1
    return result