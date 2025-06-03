bit=[0]*9
fa=[1]*9
for n in range(1,9):fa[n]=fa[n-1]*n
def up(id):
    while id<9:
        bit[id]+=1
        id+=id&(-id)
def qr(id):
    res=0
    while id:
        res+=bit[id]
        id-=id&(-id)
    return res

x=int(input())
s=list(map(int,input().split()))
z=list(map(int,input().split()))

v=''

for n in s:
    a=qr(n)
    vl=n-1-a
    v+=str(vl)
    up(n)
v=v[::-1]
r1=0
for n in range(len(v)):
    r1+=int(v[n])*fa[n]

r2=0
v=''
bit=[0]*9
for n in z:
    a=qr(n)
    vl=n-1-a
    v+=str(vl)
    up(n)
v=v[::-1]
for n in range(len(v)):
    r2+=int(v[n])*fa[n]

print(abs(r1-r2))