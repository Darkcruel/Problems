# link : https://www.hackerrank.com/challenges/append-and-delete/problem

def appendAndDelete(s, t, k):
    # Write your code here
    count = 0

    for i,j in zip(s,t):
        if i==j:
            print(i,j)
            count +=1
        else:
            break
    t_len = len(s)+len(t)
    if(t_len<=2*count+k and t_len%2==k%2 or t_len < k):
        return 'Yes'
    else:
        return 'No'