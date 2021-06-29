# link : https://www.hackerrank.com/challenges/chocolate-feast/problem

def chocolateFeast(n, c, m):
    # Write your code here
    result = n//c
    wrapper = n//c 
    while(wrapper>=m):
      result += (wrapper//m)
      wrapper = (wrapper%m) + (wrapper//m)  
    
    return result