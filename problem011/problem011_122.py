x,y = list(map(int,input().split()))
if x<y: x,y = y,x
while y!=0: x,y = y,x%y
print(x)