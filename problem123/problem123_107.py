N = int(input())
A = list(map(int, input().split()))

x = 0
for a in A:
    x ^= a

out = []
for a in A:
    out.append(str(x ^ a))

print(' '.join(out))
