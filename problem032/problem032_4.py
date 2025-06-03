def dist(x,y,p):
    tmp = 0
    for k,j in zip(x,y):
        k,j = sorted((k,j))
        tmp += (j-k)**p
    print tmp**(1/float(p))

def cheb(x,y):
    maxjk = None
    for k,j in zip(x,y):
        k,j = sorted((k,j))
        if maxjk is None:
            maxjk = j-k
        elif j-k > maxjk:
            maxjk = j-k
    print float(maxjk)

n = int(raw_input())
x = map(int,raw_input().split())
y = map(int,raw_input().split())

dist(x,y,1)
dist(x,y,2)
dist(x,y,3)
cheb(x,y)