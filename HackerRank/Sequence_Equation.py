# link : https://www.hackerrank.com/challenges/permutation-equation/problem

def permutationEquation(p):
    # Write your code here
    result = list()
    for i in range(1,len(p)+1):
        for j in range(1,len(p)+1):
            if(p[p[j-1]-1]==i):
                result.append(j)
                break
    return result
