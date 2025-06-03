n = int(input())
arr = list(map(int,input().split()))

total = 0
for i in range(n):
    total ^= arr[i]

arr = [i^total for i in arr]
print(*arr)