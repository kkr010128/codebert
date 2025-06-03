N = int(input())
A = list(map(int, input().split()))
B = list(range(1, N + 1))

A = dict(zip(A, B))
A = sorted(A.items())
ans = [str(x[1]) for x in A]


print(" ".join(ans))