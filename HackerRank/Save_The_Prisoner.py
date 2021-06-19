# link : https://www.hackerrank.com/challenges/save-the-prisoner/problem

def saveThePrisoner(n, m, s):
    # Write your code here
    if (m%n + s -1)%n == 0:
        return n
    else :
        return (m%n + s -1)%n