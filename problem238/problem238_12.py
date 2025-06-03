N, K, S = map(int, input().split())
a = [str(S)] * K

if S == 10**9:
    b = [str(1)] * (N-K)
else:
    b = [str(S+1)] * (N-K)
ans = a + b
print(*ans)