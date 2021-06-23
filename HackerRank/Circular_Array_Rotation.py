# link : https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(a, k, queries):
    # Write your code here
    result = list()
    k = k%len(a)
    for q in queries:
        result.append(a[(len(a)-k+q)%len(a)])
    return result
