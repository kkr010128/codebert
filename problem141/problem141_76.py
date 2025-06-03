(N,) = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

numLeafs = A
if not (0 <= numLeafs[0] <= 1):
    print(-1)
    exit()

# Bound max non-leaves by how many expansions the previous level can do
maxNonLeafs = [None for i in range(N + 1)]
maxNonLeafs[0] = 1 - numLeafs[0]
for i in range(1, N + 1):
    maxNonLeafs[i] = 2 * maxNonLeafs[i - 1] - numLeafs[i]
    if maxNonLeafs[i] < 0:
        print(-1)
        exit()

# Tighten max non-leaves by how many available children are on next level
maxNonLeafs[N] = 0
for i in range(N - 1, -1, -1):
    maxNonLeafs[i] = min(maxNonLeafs[i], maxNonLeafs[i + 1] + numLeafs[i + 1])


count = 0
for i in range(N + 1):
    count += maxNonLeafs[i] + numLeafs[i]
print(count)
