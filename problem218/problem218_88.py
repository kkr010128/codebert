N = int(input())
l = []
for i in range(N):
    l.append(input())
l.sort()
a = l[0]
k = [1]
n = [str(l[0])]
for i in range(1,N):
    if a == l[i]:
        k[-1] += 1
    else:
        a = l[i]
        k.append(1)
        n.append(l[i])
m = max(k)
ans = []
for i in range(len(k)):
    if k[i] == m:
        ans.append(n[i])

ans.sort()
for i in range(len(ans)):
    print(ans[i])