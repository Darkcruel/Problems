# link : https://www.hackerrank.com/challenges/non-divisible-subset/problem

def nonDivisibleSubset(k, s):
    # Write your code here
    reminder = [0]*k
    result = 0
    for item in s:
        reminder[item%k]+=1
        
    result = min(reminder[0],1)
    
    for idx in range(1,k//2+1):
        if(idx != k-idx):
            result += max(reminder[idx] , reminder[k-idx])
    if k%2==0:
        result+=1
    return result
