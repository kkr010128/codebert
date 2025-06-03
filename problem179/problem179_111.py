n, m = map(int, input().split())
a = list(map(int, input().split()))
num = sum(a)
cnt = 0
for i in range(n):
    if a[i] < num/(4*m):
        continue
    else:
        cnt += 1
if cnt >= m:
    print("Yes")
else:
    print("No")   