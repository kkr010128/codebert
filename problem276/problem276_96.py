N = int(input())
A = list(map(int, input().split()))
S = sum(A)
L = 0
for i, a in enumerate(A):
  if L + a <= S/2:
    L += a
  else:
    R = S - L
    diff = R - L
    if 2*a - diff < diff:
      L += a
      R -= a
    break
    
R = S - L
print(abs(R - L))