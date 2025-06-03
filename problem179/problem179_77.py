N, M = map(int, input().split())
A = list(map(int, input().split()))

sum = sum(A)
limit = sum / (4 * M)
A.sort(reverse = True)

ans = True
for i in range(M):
    if A[i] < limit:
        ans = False
        break
if ans:
    print("Yes")
else:
    print("No")
