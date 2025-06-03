def koch(x0,y0, x1,y1, n):
    if n == 0:
        return [(x0,y0)]
    else:
        v = (y0-y1,x1-x0)
        #print(type(n))
        #print(n[0])
        m = ((x0+x1)/2,(y0+y1)/2)
        c1 = ((2*x0+x1)/3,(2*y0+y1)/3)
        #print(m[0],n[0],m[1],n[1])
        c2x = m[0]+v[0]/(2*(3**(1/2)))
        c2y = m[1]+v[1]/(2*(3**(1/2)))
        c2 = (c2x,c2y)
        c3 = ((x0+2*x1)/3,(y0+2*y1)/3)
        return koch(x0,y0, c1[0],c1[1], n-1) \
        + koch(c1[0],c1[1], c2[0],c2[1], n-1) \
        + koch(c2[0],c2[1], c3[0],c3[1], n-1) \
        + koch(c3[0],c3[1], x1,y1, n-1)
def show_vertex(x,y):
    print("%.8f %.8f" % (x,y))

N = int(input())
V = koch(0,0,100,0,N)+[[100,0]]
for x,y in V:
    show_vertex(x,y)

