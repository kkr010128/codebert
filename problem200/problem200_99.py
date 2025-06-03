a, b, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
AB = []
for _ in range(m):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    AB.append(A[x]+B[y]-c)
AB.sort()
A.sort()
B.sort()
print(min(AB[0], A[0]+B[0]))
