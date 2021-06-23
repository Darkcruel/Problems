# link : https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

def jumpingOnClouds(c, k):
    energy = 100
    pos =0
    while 1:
        if((pos+k)%len(c)==0):
            if(c[0]==0):
                energy-=1
            else:
                energy-=3
            break
        else:
            if (c[(pos+k)%len(c)]==0):
                energy -=1
            else:
                energy -=3
            pos = (pos+k)%len(c)
    return energy