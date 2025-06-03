inf = float('inf')

def distance(p,n,x,y):
    D = 0
    s = []
    for i in range(0,n):
        s.append(x[i]-y[i])
        if s[i]<0.0:
            s[i]*=-1.0
        D += s[i]**p 
        
    if p==inf:
        return max(s)
    else:
        return D**(1.0/p)

if __name__ == '__main__':
    n = int(input())
    x = map(int,raw_input().split())
    y = map(int,raw_input().split())
        
    print float(distance(1,n,x,y))
    print float(distance(2,n,x,y))
    print float(distance(3,n,x,y))
    print float(distance(inf,n,x,y))