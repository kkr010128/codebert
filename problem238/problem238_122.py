N, K, S = map(int, input().split())
if S == 1000000000:
    fill = 1000000000 - 1
else:
    fill = S+1

print(' '.join(map(str, ([S]*K + [fill]*(N-K)))))
