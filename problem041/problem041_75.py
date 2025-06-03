X,Y,a,b,c = map(int,input().split())
if X < a + c or 0 > a - c:
    print("No")
elif Y < b + c or 0 > b - c:
    print("No")
else :
    print("Yes")
