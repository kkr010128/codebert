import sys
input = sys.stdin.readline
n,a,b=map(int,input().split())
val = n//(a+b)
pos = n%(a+b)
if pos>a:
    pos = a
print(val*a + pos)


