k, n = map(int, input().split())
A = list(map(int, input().split()))
diff = []
for i in range(n-1):
    diff.append(A[i+1] - A[i])

diff.append(A[0]+k-A[-1])
print(sum(diff)-max(diff))