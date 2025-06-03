n, m = map(int, input().split())
a = list(map(int, input().split()))
print('Yes' if len([ai for ai in a[:] if ai >= sum(a) / (4*m)]) >= m else 'No')