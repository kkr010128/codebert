import sys
import math
N = int(input())
def solve(num):
    d = math.floor(num**(1/2))
    for i in range(1,d+1):
        if num % i == 0:
            yield [i,num//i]

if N == 2:
    print(1)
    sys.exit()

cnt = 0
for a,b in solve(N-1):
    if a == b:
        cnt += 1
    else:
        cnt += 2

cnt -= 1

for s in solve(N):
    if s[0] == s[1]:
        s.pop()
    for a in s:
        if a == 1:
            continue

        tmp = N
        while True:
            tmp,m = divmod(tmp, a)
            if m == 0:
                continue
            elif m == 1:
                cnt += 1
            break

print(cnt)