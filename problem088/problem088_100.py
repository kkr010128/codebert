N, A = input(), [int(v) for v in input().split()]

# max(abs(x-y) for x, y in  zip(A, A[1:]))

stool = A[0]
ans = 0
for i, h in enumerate(A):
    if h < stool:
        ans += stool - h
    stool = max(stool, h)

print(ans)
