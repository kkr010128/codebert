n=int(input())
arr = [[False for i in range(13)] for j in range(4)]
for count in range(n):
    code = input().split()
    if (code[0]=="S"):
        arr[0][int(code[1])-1]=True
    elif (code[0]=="H"):
        arr[1][int(code[1])-1]=True
    elif(code[0]=="C"):
        arr[2][int(code[1])-1]=True
    else:
        arr[3][int(code[1])-1]=True

for i in range(4):
    if(i==0):
        img="S"
    elif(i==1):
        img="H"
    elif(i==2):
        img="C"
    else:
        img="D"
    for j in range(13):
        if(arr[i][j]==False):
            print(img+" "+str(j+1))