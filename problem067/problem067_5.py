n = int(input())
x = 0
y = 0
for _ in range(n):
    a,b=input().split()
    if a < b:
        y+=3
    elif a ==b:
        x+=1
        y+=1
    else:
        x+=3
print (x,y)
