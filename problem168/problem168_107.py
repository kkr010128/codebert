x=input()
y=x.split(" ")
n=int(y[0])
g=input()
h=g.split(" ")
su=0
for b in h:
    su+=int(b)
if(su>n):
    print(-1)
else:
    print(n-su)

