N = int(input())
p = dict()
for i in range(N):
    s = input()
    if not s in p:
        p[s] = 0
    p[s] += 1
m = max(p.values())
ans = [k for k in p.keys() if p[k] == m]
ans = sorted(ans)
for j in range(len(ans)):
    print(ans[j])