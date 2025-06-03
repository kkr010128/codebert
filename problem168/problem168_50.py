N, M = map(int, input().split())
A = [int(i) for i in input().split()]
print(N-sum(A) if N-sum(A) >= 0 else -1)