n, m, q = map(int, input().split())
a = [0]*q
b = [0]*q
c = [0]*q
d = [0]*q

A= [1] * n
for i in range(q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

ans = 0
while A[0] <= m:
    tmp = 0
    for i in range(q):
        if (A[b[i]-1] - A[a[i]-1]) == c[i]:
            tmp += d[i]
    if tmp > ans:
        ans = tmp
    
    A[-1] +=1
    for i in range(n-1,0,-1):
        if A[i] == m+1:
            A[i-1] +=1
            for j in range(len(A[i:])):
                A[i+j] = A[i-1]
print(ans)
