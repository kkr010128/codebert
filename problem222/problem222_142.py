N = int(input())
A = list(map(int,input().split()))
di = {}
for i in range(N):
    if A[i] in di:
        di[A[i]] += 1
    else:
        di[A[i]] = 1
if max(di.values()) != 1:
    print("NO")
else:
    print("YES")
