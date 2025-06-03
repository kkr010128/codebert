import math
A, B = map(int, input().split())
ans = -1
for a in range(math.ceil(A/0.08), math.ceil((A+1)/0.08)):
    if int(a*0.1) == B:
        ans = a
        break

print(ans)