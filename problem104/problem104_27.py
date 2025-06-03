import math


def LI():
    return list(map(int, input().split()))


L, R, d = LI()
Ld = (L-1)//d
Rd = R//d
ans = Rd-Ld
print(ans)
