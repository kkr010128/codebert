x,y = map(int,input().split())
y =y**2
count=0
for i in range(x):
    a,b = map(int,input().split())	
    if a**2+b**2 <=y:
        count+=1;
print(count)