# D - Teleporter
N,K = map(int,input().split())
A = [0]+list(map(int,input().split()))
s = {1:0}
l = [1]
i = 1
for j in range(1,10**10):
    i = A[i]
    if i in s:
        sigma = j-s[i]
        break
    s[i] = j
    l.append(i)
if K<s[i]:
    print(l[K])
else:
    K -= s[i]
    mod = l[s[i]:]
    print(mod[K%sigma])