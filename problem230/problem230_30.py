def main():
    import sys
    from collections import deque
    from operator import itemgetter
    M=10**10
    b=sys.stdin.buffer
    n,d,a=map(int,b.readline().split())
    m=map(int,b.read().split())
    q=deque()
    popleft,append=q.popleft,q.append
    s=b=0
    for x,h in sorted(zip(m,m),key=itemgetter(0)):
        while q and q[0]//M<x:b-=popleft()%M
        if h>b:
            t=(b-h)//a
            s-=t
            t*=a
            b-=t
            append((x+d+d)*M-t)
    print(s)
main()