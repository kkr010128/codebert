n, k = map(int, input().split())
H = list(map(int, input().split()))

L = [h for h in H if h >= k]
print(len(L))