N, K, S = map(int, input().split())

if S == 10**9:
    Ans = [S for _ in range(K)] + [1 for _ in range(N-K)]
else:
    Ans = [S for _ in range(K)] + [S+1 for _ in range(N-K)]
for ans in Ans:
    print(ans, end=' ')