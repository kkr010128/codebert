N = int(input())
A = [int(x) for x in input().split()]

B = []
for i, a in enumerate(A):
    B.append([a, i + 1])

B.sort()

ans = []
for b in B:
    ans.append(b[1])

print(*ans)

