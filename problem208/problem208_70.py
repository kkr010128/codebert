n,m=map(int,input().split())
def exit():
    import sys
    print(-1)
    sys.exit()
num=['']*n
for s,c in (map(int,input().split()) for i in range(m)):
    if n>1 and [s,c]==[1,0]:
        exit()
    if num[s-1]!='':
        if num[s-1]==c:
            continue
        else:
            exit()
    else:
        num[s-1]=c
else:
    if n==1:
        print(num[0] if num[0]!='' else 0, end='')
    else:
        print(num[0] if num[0]!='' else 1, end='')
    for i in range(1,n):
        print(num[i] if num[i]!='' else 0, end='')