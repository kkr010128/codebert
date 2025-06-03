import sys

n = int(input())
r0 = int(input())
r1 = int(input())

mx = r1-r0
mn = min(r1,r0)
l = map(int,sys.stdin.readlines())
for i in l:
    if mx < i - mn:
        mx = i - mn
    elif mn > i:
        mn = i

print(mx)