N = int(input())
A = list(map(int, input().split()))

length = len(A)
find_next = 1

for i in range(N):
    if A[i] == find_next:
        find_next += 1

if find_next == 1:
    print(-1)
else:
    print(length - find_next + 1)
