len = int(input())
arr = [0]*len

for i in range(len):
    num = int(input())
    arr[i] = num

arr = sorted(arr)
for i in range(len):
    print(arr[i])