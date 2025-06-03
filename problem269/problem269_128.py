t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
if a1>b1:
    a1, a2, b1, b2 = b1, b2, a1, a2
init = (a1-b1)*t1+(a2-b2)*t2
if init<0:
    print(0)
    exit(0)
elif init==0:
    print('infinity')
    exit(0)
lim = (b1-a1)*t1
if lim%init==0:
    print(lim//init*2)
else:
    print(lim//init*2+1)