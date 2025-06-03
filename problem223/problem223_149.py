def INT():
    return int(input())

def LI():
    return list(map(int, input().split()))

def MI():
    return map(int, input().split())

N, K = MI()
p = LI()

def E(x):
    return (x + 1) / 2

for i in range(N):
    p[i] = E(p[i])
    
ans = sum(p[:K])
E_K = ans

for i in range(N - K):
    E_K += p[i + K] - p[i]
    ans = max(ans, E_K)

print(ans)