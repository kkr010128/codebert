import math

def main():
    n = input()

    p1 = [0., 0.]
    p2 = [100., 0.]
    a = [p1,p2]
    a = rec(a,n)

    for item in a:
        print item[0], item[1]
    
def rec(a,n):
    if n == 0:
        return a
    else:
        n -= 1
        b = []
        for i in range(len(a)-1):
            p1 = a[i]
            p2 = a[i+1]
            b += koch(p1,p2)
        b.append(a[-1])
        return rec(b,n)

def koch(p1,p2):
    s  = [p1[0]+(p2[0]-p1[0])/3.,    p1[1]+(p2[1]-p1[1])/3.]
    t  = [p1[0]+2.*(p2[0]-p1[0])/3., p1[1]+2.*(p2[1]-p1[1])/3.]
    st = [t[0]-s[0],t[1]-s[1]]
    u  = [s[0]+(st[0]-math.sqrt(3)*st[1])/2., s[1]+(math.sqrt(3)*st[0]+st[1])/2.]
    return [p1,s,u,t]
    
if __name__ == "__main__":
    main()