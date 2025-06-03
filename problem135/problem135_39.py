A, B = [s for s in input().split()]

A = int(A)
B = int(float(B) * 100 + .5)

C = A * B

ans = int(C // 100)

print(ans)