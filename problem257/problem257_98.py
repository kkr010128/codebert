n = int(input())
a = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(n) :
    if a[i] == cnt + 1 :
        cnt += 1
if cnt > 0 :
    print(n-cnt)
else :
    print("-1")
