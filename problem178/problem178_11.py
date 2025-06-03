x = list(map(int,input().split()))

x[0],x[1] = x[1],x[0]
x[0],x[2] = x[2],x[0]

print(str(x[0]) +" " + str(x[1]) + " "+  str(x[2]))