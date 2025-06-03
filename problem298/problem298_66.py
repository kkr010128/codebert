N, K = map(int, input().split())
H = tuple(map(int, input().split()))
assert len(H) == N
print(len([h for h in H if h >= K]))