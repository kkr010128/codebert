N = int(input())
A = sorted([(int(a), i) for i, a in enumerate(input().split())], key = lambda x: x[0])[::-1]
X = [0] + [-1<<100] * (N + 5)
for k, (a, i) in enumerate(A):
    X = [max(X[j] + abs(N - (k - j) - 1 - i) * a, X[j-1] + abs(j - 1- i) * a if j else 0) for j in range(N + 5)]
print(max(X))