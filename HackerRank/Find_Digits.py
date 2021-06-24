# link : https://www.hackerrank.com/challenges/find-digits/problem

def findDigits(n):
    # Write your code here
    divisor = list()
    result = 0
    copy_n = n
    while copy_n !=0:
        divisor.append(copy_n%10)
        copy_n = copy_n // 10
    
    for i in divisor:
        if(i!=0 and n%i==0):
            result+=1
    return result
