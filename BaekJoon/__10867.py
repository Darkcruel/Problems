len = int(input())
arr = input().split()

for i in range(len):
    arr[i] = int(arr[i])

arr2 = sorted(list(set(arr[0:len])))
for i in arr2:
    print(i , end=" ")