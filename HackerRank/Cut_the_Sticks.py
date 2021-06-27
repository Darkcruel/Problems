# link : https://www.hackerrank.com/challenges/cut-the-sticks/problem

def cutTheSticks(arr):
    # Write your code here
    result = list()

    while 1:
        if(len(arr)==0):
            return result
        else:
            temp = list()
            result.append(len(arr))
            length_of_cut = min(arr)
            for idx in range(len(arr)):
                if arr[idx] == length_of_cut:
                    arr[idx] = 0
                else:
                    arr[idx] -= length_of_cut
                
                if(arr[idx] !=0):
                    temp.append(arr[idx])
            arr = temp
                    