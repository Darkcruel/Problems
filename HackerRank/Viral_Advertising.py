# link : https://www.hackerrank.com/challenges/strange-advertising/problem

def viralAdvertising(n):
    # Write your code here
    result = 0
    liked = 0
    Shared = 5
    day = 1
    while(day<=n):
        liked = Shared//2;
        result += liked
        Shared = 3 * liked
        day = day+1
    return result