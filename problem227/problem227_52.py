n, k = map(int, input().split())
h = sorted(list(map(int, input().split())), reverse = True)

del h[:k]
print(sum(h))
