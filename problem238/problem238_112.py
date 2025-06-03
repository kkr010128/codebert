N, K, S = map(int, input().split())
rem = 1 if S >= 10**9 else S+1
ret = [S]*K + [rem]*(N-K)
print(' '.join(map(str, ret)))