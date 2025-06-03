n = int(input())
a = list(map(int, input().split()))
 
target = 1
for i in range(n):
    if a[i] == target:
        target += 1
if target >= 2:
    print(n - target + 1)
else:
    print(-1)