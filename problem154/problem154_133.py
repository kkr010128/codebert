N, K = map(int, input().split())
Have = set([])
for _ in range(K):
    _ = input()
    Have |= set(map(int, input().split()))
print(N-len(Have))