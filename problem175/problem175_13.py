from collections import Counter
N = int(input())
S = input()
c = Counter(S)
ans = c['R'] * c['G'] * c['B']

for s in range(N-2):
    for d in range(1, (N-1-s)//2+1):
        t = s + d
        u = t + d
        if S[s] != S[t] and S[t] != S[u] and S[u] != S[s]:
            ans -= 1
print(ans)
