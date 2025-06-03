N,X,T = map(int, input().split())

nf = float(N/X)
ni = int(N/X)
d = nf - ni 

if d == 0:
    ans = ni * T
else:
    ans = (ni + 1) * T

print(ans)