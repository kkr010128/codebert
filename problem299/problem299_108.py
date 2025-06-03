n = int(input())
A = list(map(int, input().split()))

N = list(range(1, n + 1))
c = sorted(zip(A, N))
A, N = zip(*c)

print(*N)
