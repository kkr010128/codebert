N = int(input())
ToF = []
for i in range(N):
    A = list(map(int,input().split()))
    A.sort()
    if A[0]**2 + A[1]**2 == A[2]**2:
        ToF.append("YES")
    else:
        ToF.append("NO")
for i in ToF:
    print(i)