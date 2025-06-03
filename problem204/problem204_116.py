s=input()
q=int(input())
quary=[]
for i in range(q):
    temp=list(input().split())
    quary.append(temp)
switch=False
first=''
last=''
for i in range(q):
    if quary[i][0]=='1':
        if switch:
            switch=False
        else:
            switch=True

    else:
        if quary[i][1]=='1':
            if switch:
                last+=quary[i][2]
            else:
                first+=quary[i][2]
        else:
            if switch:
                first+=quary[i][2]
            else:
                last+=quary[i][2]
s=first[::-1]+s+last
if switch:
    print(s[::-1])
else:
    print(s)