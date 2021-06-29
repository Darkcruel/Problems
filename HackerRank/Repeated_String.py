# link : https://www.hackerrank.com/challenges/repeated-string/problem

def repeatedString(s, n):
    # Write your code here
    set_of_string = list(set(s))
    if(len(set_of_string)==1 and set_of_string[0]=='a'):
        return n
    result = 0
    for alpha in s:
        if(alpha == 'a'):
            result +=1
    result = result * (n//len(s))
    for alpha in s[:(n%len(s))]:
        if(alpha == 'a'):
            result +=1
    return result