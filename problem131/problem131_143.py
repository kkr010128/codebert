import sys
a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
if v==w or w>v:
    print('NO')
    sys.exit()
else:
    tp=(b-a)/(v-w)
    tm=(a-b)/(v-w)
    if b>a:
        if t>=tp:
            print('YES')
        else:
            print('NO')
    else:
        if t>=tm:
            print('YES')
        else:
            print('NO')

