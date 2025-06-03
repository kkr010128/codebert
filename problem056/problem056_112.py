(n,m) = [int(i) for i in input().split()]

A = []
for nc in range(n):
    A.append([int(i) for i in input().split()])

b = []
for mc in range(m):
    b.append(int(input()))

product = []
for nc in range(n):
    total = 0
    for mc in range(m):
        total += A[nc][mc] * b[mc]

    product.append(total)

[print(p) for p in product]