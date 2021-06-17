# link : https://www.hackerrank.com/challenges/angry-professor/problem

def angryProfessor(k, a):
    # Write your code here
    count = 0
    for i in range(len(a)):
        if a[i]<=0:
            count+=1
    if(count < k):
        return 'YES'
    else:
        return 'NO'