def solve(i,x1,x2,y1,y2):
    global n
    if i == n:
        return print(x2,y2)
    X1 = (2*x1+x2)/3
    Y1 = (2*y1+y2)/3
    X3 = (x1+2*x2)/3
    Y3 = (y1+2*y2)/3
    X2 = (X3+X1)/2+3**(0.5)*(Y1-Y3)/2
    Y2 = (3**(0.5)*(X3-X1)+(Y1+Y3))/2
    solve(i+1,x1,X1,y1,Y1)
    solve(i+1,X1,X2,Y1,Y2)
    solve(i+1,X2,X3,Y2,Y3)
    solve(i+1,X3,x2,Y3,y2)

n = int(input())
print(0,0)
solve(0,0,100,0,0)
