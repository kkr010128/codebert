h1, m1, h2, m2, k = map(int,input().split())
 
h=h2 - h1
if h < 0:
    h = 24+h
    m=m2 - m1
    du=h*60+m-k
elif h == 0:
    if m1 < m2:
        du = m2-m1-k
    else:
        du = 24*60 +(m2-m1)-k
else:
    du = h*60+(m2-m1)-k
        
print(du)