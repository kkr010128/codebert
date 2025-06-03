a,b,c=map(int,input().split())
y=0

for i in range(b-a+1):
    j=1
    while (i+a)*j <= c:
        if (i+a)*j==c:
            y+=1
            break
        j+=1
print(y)
