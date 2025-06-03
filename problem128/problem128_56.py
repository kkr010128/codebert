l=input()
ls=l.split(" ")
X=int(ls[0])
N=int(ls[1])
lstr=input()
lst=lstr.split(" ")
fl=[]
if(N!=0):
    for a in lst:
         fl.append(int(a))
for a in range(101):
    if(X-a not in fl):
         print(X-a)
         break
    if(X+a not in fl):
         print(X+a)
         break