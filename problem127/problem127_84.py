x,y = map(int,input().split())
A = y//2
B = (x-A)
while A>-1:
    if y==2*A + 4*B:
        print("Yes")
        break
    A = A-1
    B = B+1
    if A==-1:
        print("No")