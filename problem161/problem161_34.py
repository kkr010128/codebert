ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a,b,n=nm()

import math

print(math.floor(a*(min(b-1,n)%b)/b))