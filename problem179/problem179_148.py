count = 0
n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] >= sum(a)/4/m:
        count += 1
if count >= m:
    print("Yes")
else:
    print("No")