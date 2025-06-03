n = int(input())
arr = [0] * n

for i in input().split():
    i = int(i)
    arr[i - 1] += 1

for i in range(n):
    print(arr[i])