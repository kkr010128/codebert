P = [1 for _ in range(10**6)]
P[0]=0
P[1]=0
for i in range(2,10**3):
    for j in range(i*i,10**6,i):
        P[j] = 0
Q = []
for i in range(2,10**6):
    if P[i]==1:
        Q.append(i)
N = int(input())
C = {}
for q in Q:
    if N%q==0:
        C[q] = 0
        while N%q==0:
            N = N//q
            C[q] += 1
if N>1:
    C[N] = 1
cnt = 0
for q in C:
    k = C[q]
    n = 1
    while k>(n*(n+1))//2:
        n += 1
    if k==(n*(n+1))//2:
        cnt += n
    else:
        cnt += n-1
print(cnt)
