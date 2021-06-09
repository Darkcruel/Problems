# link : https://www.hackerrank.com/challenges/electronics-shop/problem

def getMoneySpent(keyboards, drives, b):

    result = 0
    keyboards.sort()
    drives.sort()
    
    if(keyboards[0]+drives[0]>b):
        return -1
    
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if(keyboards[i]+drives[j]<=b and result<= keyboards[i]+drives[j]):
                result = keyboards[i]+drives[j]
    return result