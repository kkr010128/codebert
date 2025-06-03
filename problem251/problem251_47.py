
#<D>wa
n, k = map(int,input().split())
r, s, p = map(int,input().split())
q = input()
d = {"r":p,"s":r, "p":s}
ans = 0
wins = [False] * k
for i in range(len(q)):
    if not wins[i % k] or q[i] != q[i - k]:
        ans += d[q[i]]
        wins[i % k] = True
    else:
        wins[i % k] = False
print(ans)        
