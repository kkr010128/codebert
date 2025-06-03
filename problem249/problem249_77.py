x=list(map(int,input().split()))

if x[0]>x[2]:
    print(str(x[0]-x[2])+" "+str(x[1]))
elif x[0]+x[1]>x[2]:
    print("0"+" "+str(x[0]+x[1]-x[2]))
else:
    print("0"+" "+"0")