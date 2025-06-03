from sys import stdin
def ip():
    return stdin.readline().rstrip()
d,t,s=map(int,ip().split())
if d<=t*s:
    print('Yes')
else:
    print('No')