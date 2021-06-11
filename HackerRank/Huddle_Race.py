# link :https://www.hackerrank.com/challenges/the-hurdle-race/problem

def hurdleRace(k, height):
    # Write your code here
    high = set()
    for i in range(len(height)):
        high.add(height[i])
    
    if(max(high) == k or max(high)<k):
        return 0
    else:
        return (max(high))-k