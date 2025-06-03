H, W, M, *HW = map(int, open(0).read().split())
HW = list(zip(*[iter(HW)] * 2))

A = [0] * (H + 1)
B = [0] * (W + 1)
for h, w in HW:
    A[h] += 1
    B[w] += 1

a = max(A)
b = max(B)

cnt = A.count(a) * B.count(b) - len([0 for h, w in HW if A[h] == a and B[w] == b])

print(a + b - (cnt == 0))