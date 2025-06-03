import copy
n,k,*A = map(int,open(0).read().split())
for _ in range(min(50,k)):
    B = [0] * (n+1)
    for i,d in enumerate(A):
        start = max(0,i-d)
        B[start] += 1
        end = min(n,i+d+1)
        B[end] -= 1
    light = 0 
    for i,b in enumerate(B[:n]):
        light += b
        A[i] = light

print(*A)
