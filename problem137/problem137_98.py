n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if n % 2:
    l = A[n // 2]
    r = B[n // 2]
    ans = r - l + 1
    print(ans)
else:
    l = A[n // 2 - 1] + A[n // 2]
    r = B[n // 2 - 1] + B[n // 2]
    ans = r - l + 1
    print(ans)
