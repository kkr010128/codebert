X=int(input())
a=[]
for i in range(1,X+1):
    a.append(360*i)
for k in range(len(a)):
    if a[k]%X==0:
        print(int(a[k]//X))
        break