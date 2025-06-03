data=input()
x = data.split(" ")
tmp=x[2]
x[2]=x[1]
x[1]=x[0]
x[0]=tmp
print(x[0],x[1],x[2])