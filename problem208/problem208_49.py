n, m = map(int,input().split())
sc = [list(map(int,input().split())) for _ in range(m)]

ans = -1

for i in range(1000):
    s_i = str(i)
    if len(s_i) == n and all(int(s_i[s-1])==c for s,c in sc):
        ans = i
        break

print(ans)