# link : https://www.hackerrank.com/challenges/bon-appetit/problem

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    total = 0
    for i in range(len(bill)):
        if(i!=k):
            total += bill[i]
    
    total = total // 2
    if(total == b):
        print('Bon Appetit')
    else:
        print(abs(total - b))
