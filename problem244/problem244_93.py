def ma():
    return map(int,input().split())
k,x=ma()
if k*500>=x:
    print('Yes')
else:
    print('No')