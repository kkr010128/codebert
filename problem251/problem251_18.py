N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())
for i in range(N):
    if i >= K and T[i-K] == T[i]:
        T[i] = 'a'
ans = 0
for i in T:
    if i == 'r':
        ans += P
    elif i == 's':
        ans += R
    elif i == 'p':
        ans += S
print(ans)