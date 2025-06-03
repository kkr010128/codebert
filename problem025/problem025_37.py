input()
A = [int(x) for x in input().split()]
input()
ms = [int(x) for x in input().split()]

enable_create = [False]*2000
for bit in range(1 << len(A)):
    n = 0
    for i in range(len(A)):
        if 1 & (bit >> i) == 1:
            n += A[i]
    enable_create[n] = True

for m in ms:
    print("yes" if enable_create[m] else "no")