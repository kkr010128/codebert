N, K, S = map(int, input().split())

x = 10**9
for i in range(2, S):
    if S % i != 0:
        x = i
        break

res = [S]*K + [x]*(N-K)
print(" ".join(map(str, res)))