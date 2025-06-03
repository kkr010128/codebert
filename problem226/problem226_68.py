H,N=map(int,input().split())
list=[]
for i in map(int,input().split()):
    list.append(i)
if H - sum(list) <= 0:
    print('Yes')
else:
    print('No')


