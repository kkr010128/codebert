N = int(input())
M0 = M1 = -float('inf')
m0 = m1 = float('inf')

for _ in range(N):
    x, y = map(int, input().split())
    M0 = max(M0, x - y)
    m0 = min(m0, x - y)
    M1 = max(M1, x + y)
    m1 = min(m1, x + y)

print(max(M0 - m0, M1 - m1))