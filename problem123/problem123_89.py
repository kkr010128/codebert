N = int(input())
arr = list(map(int, input().split()))
s = 0
for i in range(N):
    s ^= arr[i]
for i in range(N):
    arr[i] ^= s
print(' '.join(map(str, arr)))