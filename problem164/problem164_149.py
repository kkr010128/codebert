A,B,C,D=map(int,input().split())
x=(A-1)//D+1
y=(C-1)//B+1
if x<y:
    print("No")
else:
    print("Yes")
