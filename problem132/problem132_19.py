N,K = map(int,input().split())
A = list(map(int,input().split()))
R = [N]*N
def update(A):
    b = [0]*N
 
    for i,a in enumerate(A):
        l = max(0,i-a)
        r = min(N-1,i+a)
 
        b[l] += 1
        if r+1 < N:
            b[r+1] -= 1
    
    res = []
    s = 0
    for i in b:
        s += i
        res.append(s)
    return res
 
for _ in range(K):
    A = update(A)
    if A == R:
      break
print(*A)
