N, K = map(int, input().split())
A = list()

for i in range(K):
    input()
    A.extend(list(map(int, input().split())))

print(N - len(set(A)))
