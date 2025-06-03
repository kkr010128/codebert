import math
n = int(input())
m = math.floor(math.sqrt(n)) + 1
ans = 10**12

for a in range(1,m+1):
    b = n/a
    if b.is_integer():
        move = a+b-2
    else:
        continue
    ans = min(ans,move)
print(int(ans))