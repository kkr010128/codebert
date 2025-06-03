def koch(d,p0,p1):
    #終了条件
    if d == n:
        return
    
    #内分点：s,t
    s=[(2*p0[0]+p1[0])/3,(2*p0[1]+p1[1])/3]
    t=[(2*p1[0]+p0[0])/3,(2*p1[1]+p0[1])/3]
    
    #正三角形の頂点:u
    u=[(p0[0]+p1[0])/2-(p1[1]-p0[1])*(3**(1/2)/6),(p1[1]+p0[1])/2+(p1[0]-p0[0])*(3**(1/2)/6)]
    
    koch(d+1,p0,s)
    print(*s)
    # point.append(s)
    koch(d+1,s,u)
    print(*u)
    # point.append(u)
    koch(d+1,u,t)
    print(*t)
    # point.append(t)
    koch(d+1,t,p1)
    
p0=[0,0]
p1=[100,0]


n=int(input())

print(*p0)
koch(0,p0,p1)
print(*p1)

