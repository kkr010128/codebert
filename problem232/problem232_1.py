a,b = map(int,input().split())
l=[]
if a>=b:
    for i in range(a):
        l.append(b)
else:
    for i in range(b):
        l.append(a)

print(''.join(map(str,l)))