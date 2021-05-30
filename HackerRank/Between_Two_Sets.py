# link : https://www.hackerrank.com/challenges/between-two-sets/problem

# Input 
# a : int array
# b : int array

def getTotalX(a, b):
    # Write your code here
    a.sort()
    b.sort()
    result = 0 
    gcd = 1
    
    for i in range(1,b[-1]+1):
        flag = True
        for j in range(len(b)):
            if (b[j]%i!=0):
                flag = False
                break
        if(flag==True and gcd<i):
            gcd = i
    
    for i in range(1,gcd+1):
        flag = True
        for j in range(len(a)):
            if (i%a[j]!=0 or gcd%i!=0):
                flag = False
                break
        if(flag == True):
            result += 1
            print(i)
    return result
        