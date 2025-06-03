from collections import deque
D1 = {i:chr(i+96) for i in range(1,27)}
D2 = {val:key for key,val in D1.items()}

N = int(input())
heap = deque([(D1[1],1)])
A = []
while heap:
    a,n = heap.popleft()
    if n<N:
        imax = 0
        for i in range(len(a)):
            imax = max(imax,D2[a[i]])
        for i in range(1,min(imax+1,26)+1):
            heap.append((a+D1[i],n+1))
    if n==N:
        A.append(a)
A = sorted(list(set(A)))
for i in range(len(A)):
    print(A[i])