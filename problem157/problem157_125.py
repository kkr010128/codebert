n=int(input())
a=list(map(int,input().split()))
f={}
f2={}
for i in range(n):
    z=i+a[i]
    z1=i-a[i]
    #print(z,z1)
    try:
        f[z]+=1
    except:
        f[z]=1
    try:
        f2[z1]+=1
    except:
        f2[z1]=1
s=0
for i in f.keys():
    if(i in f2):
        s+=f[i]*f2[i]
print(s)
