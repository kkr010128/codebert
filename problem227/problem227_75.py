N, K = map(int, input().split())
H = sorted(list(map(int, input().split())))
print(sum(H[:N - K]) if not N <= K else 0)
