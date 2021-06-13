# link : https://www.hackerrank.com/challenges/picking-numbers/problem

def pickingNumbers(a):
    # Write your code here
    set_a = set(a) # set of a
    result = 0
    for i in set_a:
        count = list()
        for j in a:
            if(j==i or j==i+1):
                count.append(j)
        count.sort()
        if(len(count)>=result):
            result = len(count)
    return result 