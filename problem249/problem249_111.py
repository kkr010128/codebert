A, B, K = map(int, input().split())
if A >= K:
    print(str(A - K) + ' ' + str(B))
else:
    print(str(0) + ' ' + str(max((B - (K - A)), 0)))
