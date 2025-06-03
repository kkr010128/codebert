a,b = map(int,input().split())
x = int(a // b)
y = int(a - b*x)
z = a / b


print(x,y,f"{z:.5f}")
