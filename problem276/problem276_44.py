N = int(input())
arr = list(map(int, input().split()))
first = 0
second = sum(arr)
min_delta = second - first
for i in range(N):
    first += arr[i]
    second -= arr[i]
    min_delta = min(abs(second - first), min_delta)

print(min_delta)
