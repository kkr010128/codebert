n = int(input())
A = list(map(int, input().split()))
N = sorted(range(1, n + 1), key=lambda x: A[x - 1])
print(*N)