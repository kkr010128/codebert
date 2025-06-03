N, K = map(int, input().split())
d = []
A = [[] for i in range(K)]

for i in range(K):
    d.append(int(input()))
    A[i] = list(map(int, input().split()))

hold = set()
for i in range(len(A)):
    hold = hold | set(A[i])

print(N - len(hold))