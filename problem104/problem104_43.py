import sys

read = sys.stdin.read
readline = sys.stdin.readline
count = 0
l, r, d= [int(x) for x in readline().rstrip().split()]
#print(l,r,d)
for i in range(l,r+1):
    if i % d == 0:
        count += 1

print(count)
