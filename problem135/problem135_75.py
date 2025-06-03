a,b= input().split()

a = int(a)
b,c = map(int,b.split("."))

print(a*(100*b+c)//100)
