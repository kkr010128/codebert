a,b,c = map(int,input().split())
if c < a+b:
    print("No")
else:
    if 2*a*b < c*c + a*a + b*b -2*(a*c+b*c):
        print("Yes")
    else:
        print("No")