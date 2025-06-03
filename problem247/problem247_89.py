def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
 
def div_ceil(x, y): return (x + y - 1) // y
 
N, M = map(int, input().split())
*A, = map(int, input().split())
A = list(set([a // 2 for a in A]))
L = A[0]
for a in A[1:]:
    L *= a // gcd(L, a)
for a in A:
    if (L // a) % 2 == 0:
        ans = 0
        break
else:
    ans = div_ceil(M // L, 2)
print(ans)