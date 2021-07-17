# link : https://www.hackerrank.com/challenges/encryption/problem

def encryption(s):
    # Write your code here
    row = 0 
    col = 0
    conv = list()
    result = ''
    for i in range(1,10):
        if(i * i <= len(s) and (i+1)*(i+1)>=len(s)):
            if(i*i == len(s)):
                row = i
                col = i
            else:
                row = i
                col = i+1
            break
    if(row*col<len(s)):
        row += 1
        
    for idx in range(row):
        conv.append(s[idx*col:(idx+1)*col])
    
    for i in range(col):
        for j in range(row):
            if((col*j)+i< len(s)):
                result+= conv[j][i]
        result += ' '
    return result