N = int(input())
A = sorted(list(map(int,input().split())))
ans = "YES"

for i in range(1,N,2):
    boollist = [ A[i-1] == A[i] ]
    if i < N-1 :
        boollist.append(A[i] == A[i+1])
    if any(boollist):
        ans = "NO"
        break
print(ans)