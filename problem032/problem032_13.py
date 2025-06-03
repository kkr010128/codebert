def dist(x,y,p):
    d = 0
    for i in range(len(x)):
        d += abs(x[i]-y[i])**p
    d = d**(1/p)
    return d

n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
print('{0:.6f}'.format(dist(x,y,1)))
print('{0:.6f}'.format(dist(x,y,2)))
print('{0:.6f}'.format(dist(x,y,3)))
print('{}'.format(max([abs(x[i]-y[i])for i in range(n)])))
