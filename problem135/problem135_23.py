N = list(input().split())
A = int(N[0])
b1,b2 = N[1].split('.')
B = int(b1+b2)
prd = list(str(A*B))
ans = 0
if len(prd) < 3:
    ans = 0
else:
    prd.pop()
    prd.pop()
    ans = int(''.join(prd))
print(ans)
