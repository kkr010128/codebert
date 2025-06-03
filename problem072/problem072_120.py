n = int(input())
d = []
for i in range(n):
    a,b = map(int,input().split())
    d.append([a,b])
cnt,ans = 0,0
for i in d:
    if i[0] == i[1]:
        cnt += 1
        ans = max(ans,cnt)
    else:
        cnt = 0
if ans>2:
    print("Yes")
else:
    print("No")