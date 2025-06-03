A, B = [int(_) for _ in input().split()]
aa = [int(i * 0.08) for i in range(1, 10000)]
bb = [int(i * 0.1) for i in range(1, 10000)]
for i, a, b in zip(range(1, 10000), aa, bb):
    if (a, b) == (A, B):
        print(i)
        exit()
print(-1)
