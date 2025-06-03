x = list(map(int, input().split()))
d = list(input())
for i in d:
    if i == 'S':
        t=x[1]
        x[1]=x[0]
        x[0]=x[4]
        x[4]=x[5]
        x[5]=t
    elif i == 'N':
        t=x[1]
        x[1]=x[5]
        x[5]=x[4]
        x[4]=x[0]
        x[0]=t
    elif i == 'E':
        t=x[2]
        x[2]=x[0]
        x[0]=x[3]
        x[3]=x[5]
        x[5]=t
    elif i == 'W':
        t=x[2]
        x[2]=x[5]
        x[5]=x[3]
        x[3]=x[0]
        x[0]=t
print(x[0])