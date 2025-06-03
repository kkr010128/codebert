import math

def koch(d, a, b):
    if d== 0:
        return
    s=[0,0]
    t=[0,0]
    u=[0,0]
    
    s[0] = (2.0*a[0]+1.0*b[0])/3.0
    s[1] = (2.0*a[1]+1.0*b[1])/3.0
    t[0] = (1.0*a[0]+2.0*b[0])/3.0
    t[1] = (1.0*a[1]+2.0*b[1])/3.0
    u[0] = (t[0] - s[0])*math.cos(math.radians(60))-(t[1] - s[1])*math.sin(math.radians(60)) + s[0]
    u[1] = (t[0] - s[0])*math.sin(math.radians(60))+(t[1] - s[1])*math.cos(math.radians(60)) + s[1]
    
    koch(d-1,a,s)
    print("{:.8f}".format(s[0]), "{:.8f}".format(s[1]))  
    koch(d-1,s,u)
    print("{:.8f}".format(u[0]), "{:.8f}".format(u[1]))  
    koch(d-1,u,t)      
    print("{:.8f}".format(t[0]), "{:.8f}".format(t[1]))  
    koch(d-1, t, b)

n = int(input())

p1=[0,0]
p2=[100,0]

print("{:.8f}".format(p1[0]), "{:.8f}".format(p1[1]))
koch(n, p1, p2)
print("{:.8f}".format(p2[0]), "{:.8f}".format(p2[1]))


