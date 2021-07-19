# link : https://www.hackerrank.com/challenges/kaprekar-numbers/problem

def kaprekarNumbers(p, q):
    # Write your code here
    result = list()
    for num in range(p,q+1):
        square = str(num*num)
        if(len(square)==1):
            if(num*num == num):
                result.append(num)
        else:
            if(int(square[0:len(square)//2])+int(square[len(square)//2:])==num):
                result.append(num)    
    if(len(result)==0):
        print('INVALID RANGE')
    else:
        for i in result:
            print(i , end=' ')
        
