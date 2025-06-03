n = int(input())
s = input().split()
arr = [int(s[i]) for i in range(n)]
arr.sort()
sum = 0
for i in range(len(arr)):
    sum += arr[i]
print(arr[0], arr[len(arr)-1], sum)