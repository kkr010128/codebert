import math

def rot60(s,t):
    v=t-s
    a=1/2+complex(0,(math.sqrt(3)/2))
    return v*a+s

def puts(p):
    x=p.real
    y=p.imag
    print('{real} {imaginary}'.format(real=x,imaginary=y))

def koch(p1, p2, n):
    if n==0:
        return

    s=(p2-p1)*(1/3)+p1
    t=(p2-p1)*(2/3)+p1
    u=rot60(s,t)
    koch(p1,s,n-1)
    puts(s)
    koch(s,u,n-1)
    puts(u)
    koch(u,t,n-1)
    puts(t)
    koch(t,p2,n-1)
    
n=int(input())
s=complex(0,0)
t=complex(100,0)
puts(s)
koch(s,t,n) 
puts(t)
