import sys

n = int(input())
r0 = int(input())
r1 = int(input())
mx = r1-r0
mn = min(r1,r0)

for i in map(int,sys.stdin.readlines()):
    if mx < i - mn:
        mx = i - mn
        if 0 > i-mn:
            mn = i
    elif mn > i:
        mn = i

print(mx)