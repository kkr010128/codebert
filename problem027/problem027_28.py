import cmath
def f():
 global d
 p=[]
 for i in range(len(d)-1):
  a,b=d[i],d[i+1]
  r=(b-a)/3
  p+=[a,a+r,a+r+r*cmath.rect(1,cmath.pi/3),b-r]
 d=p+[d[-1]]
d=[0j,100+0j]
for _ in[0]*int(input()):f()
for e in d:print(e.real,e.imag)
