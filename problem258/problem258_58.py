import math
n = int(input())
cnt = 0
mod = 10
if n%2 == 1:
    print(0)
    exit()
while mod<=n:
    cnt += n//mod
    mod*=5
print(cnt)
