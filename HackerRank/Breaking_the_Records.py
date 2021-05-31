# link : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores):
    # Write your code here
    result = [0,0]
    low = scores[0]
    high = scores[0]
    for i in range(len(scores)):
        if(scores[i]>high):
            high = scores[i]
            result[0]+=1
        elif(scores[i]<low):
            low = scores[i]
            result[1]+=1
    return result