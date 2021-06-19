# link : https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def beautifulDays(i, j, k):
    # Write your code here
  
    result = 0
    
    for day in range(i,j+1):
        reverse_day = int(str(day)[::-1])
        if(abs(day - reverse_day)%k==0):
            result += 1
            
    return result