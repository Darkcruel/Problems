# Problem link : https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    in_apples = 0
    in_oranges = 0
    for i in range(len(apples)):
        apples[i] = apples[i]+a
        if((s<=apples[i]) and (apples[i]<=t)):
            in_apples +=1
    for i in range(len(oranges)):
        oranges[i] += b
        if((s<=oranges[i]) and (oranges[i]<=t)):
            in_oranges += 1
    print(in_apples)
    print(in_oranges)
    