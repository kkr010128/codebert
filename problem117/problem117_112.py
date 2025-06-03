import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,k = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))

sa = [0]*(n+1)
sb = [0]*(m+1)

for i in range(n):
    sa[i+1] = sa[i]+a[i]
for i in range(m):
    sb[i+1] = sb[i]+b[i]

isb=m
ans = 0
for isa in range(n+1):
    if sa[isa]>k:
        break
    #while isb>0 and sa[isa]+sb[isb]>k:
    while sa[isa]+sb[isb]>k:
        isb-=1
    ans = max(ans, isa+isb)
    
print(ans)