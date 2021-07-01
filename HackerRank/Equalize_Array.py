# link : https://www.hackerrank.com/challenges/equality-in-a-array/problem

def equalizeArray(arr):
    # Write your code here
    result =list()
    element = list(set(arr))
    for item in element:
        count = 0
        for idx in range(len(arr)):
            if(item !=arr[idx]):
                count+=1
        result.append(count)
    return min(result)
