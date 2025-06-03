ri = lambda S: [int(v) for v in S.split()]
def rii(): return ri(input())
 
H, N = rii()
A = rii()

print("Yes" if H - sum(A) <= 0 else "No")