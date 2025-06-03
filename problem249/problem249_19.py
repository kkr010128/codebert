A, B, K = map(int, input().split())
if A <= K:
    B -= K - A
    if B < 0:
        B = 0
    A = 0
else:
    A -= K
print(A, B)
