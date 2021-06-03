# link : https://www.hackerrank.com/challenges/migratory-birds/problem

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    count = dict()
    result = 0
    max_count = 0
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    res = sorted(count.items())
    for i in res:
        if i[1]>max_count:
            result = i[0]
            max_count = i[1]
        elif i[1] == max_count and i[0]<result:
            result = i[0]
            max_count = i[1]
    return result
            