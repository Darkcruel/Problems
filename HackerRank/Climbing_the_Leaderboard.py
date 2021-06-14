# link : https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def climbingLeaderboard(scores, player):
    scores = sorted(list(set(scores)))
    index = 0
    result = []
    n = len(scores)
    for i in player:
        while (n > index and i >= scores[index]):
            index += 1
        result.append(n+1-index) 
    return result