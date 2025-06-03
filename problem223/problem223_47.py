N, K = map(int, input().split())
p = list(map(int, input().split()))


def calc(x):
    return (x+1)/2


pe = []
for i in range(N):
    pe.append(calc(p[i]))

cs = [pe[0]] + [0]*(N-1)

for i in range(1, N):
    cs[i] = pe[i] + cs[i-1]

ans = cs[K-1]
for i in range(K, N):
    wa = cs[i] - cs[i-K]
    ans = max(ans, wa)

print(ans)



