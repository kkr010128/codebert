a,b=map(str,input().split())
a=int(a)
b=100*int(b[0])+10*int(b[2])+1*int(b[3]) #bを100倍した値(整数)に直す
print((a*b)//100)