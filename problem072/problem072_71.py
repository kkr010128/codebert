a = int(input())
l = []
c,f =0, 0
for i in range(a):
    ta,tb = map(int,input().split())
    if ta==tb : c+=1
    else: c = 0
    if c>=3 : f = 1
if f:
    print("Yes")
else:
    print("No")
