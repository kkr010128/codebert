n = int(input())
ss = [input() for _ in range(n)]

cnt = {}
ans =0
for s in ss:
    if s not in cnt:
        cnt[s]=0
        ans += 1
print(ans)
    
