# link : https://www.hackerrank.com/challenges/bigger-is-greater/problem

def biggerIsGreater(w):
    # Write your code here
    cutter = -1
    for idx in range(len(w)-1,0,-1):
        if(w[idx] > w[idx-1]):
            cutter = idx
            break
    
    if(cutter==-1):
        return 'no answer'
    down_w = sorted(w[cutter:])
    replace = ""
    for idx in range(len(down_w)):
        if w[cutter-1] < down_w[idx]:
            replace = w[cutter-1]
            w = w[:cutter-1] + down_w[idx] + w[cutter:]
            down_w.remove(down_w[idx])
            down_w.append(replace)
            break
    down_w.sort()
    w = w[:cutter]
    for idx in range(len(down_w)):
        w = w + down_w[idx]
    
    return w