N, K = map(int, input().split())
hlist = list(map(int, input().split()))
print(len([x for x in hlist if x >= K]))
