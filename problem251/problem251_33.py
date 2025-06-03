n, k = list(map(int, input().split(' ')))
r, s, p = list(map(int, input().split(' ')))
d = dict(r=p,
         s=r,
         p=s)
ttt = input()
ans = 0
prevs = []
for i in range(n):
    if i < k or ttt[i] != prevs[i-k]:
        ans += d[ttt[i]]
        prevs.append(ttt[i])
    else:
        prevs.append('hoge')
print(ans)
