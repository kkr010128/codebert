N = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0
di = A[0] + 111
for i in A:
    if di != i:
        count += 1
    di = i
if count == N:
    print("YES")
else:
    print("NO")