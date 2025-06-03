import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


t1,t2 = map(int, input().split())
a1,a2 = map(int, input().split())
b1,b2 = map(int, input().split())

a1 *= t1
a2 *= t2
b1 *= t1
b2 *= t2

if a1+a2==b1+b2:
    ans = "infinity"
else:
    if a1+a2 < b1+b2:
        a1,a2,b1,b2 = b1,b2,a1,a2
    # a1+a2が大きい
    if a1>b1:
        ans = 0
    else:
        ans = ((b1-a1) // (a1+a2-b1-b2)) * 2 + 1
        if (b1-a1) % (a1+a2-b1-b2) ==0:
            ans -= 1
print(ans)    