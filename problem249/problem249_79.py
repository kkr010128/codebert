A, B, K = map(int, input().split())

if A >= K:
    A -= K
    K = 0
else:
    K -= A
    A = 0

if B >= K:
    B -= K
else:
    B = 0

print(A, B)
