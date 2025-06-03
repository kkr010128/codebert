A,B = map(int,input().split())
x = A
y = B
while y>0:
    x,y = y,x%y
print((A//x)*B)