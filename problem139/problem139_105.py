import math

h1,m1,h2,m2,k=map(int,input().split())
start=60*h1+m1
end=60*h2+m2


print(end-start-k)
"""

a=[]
temp=input().split()
for i in range(n):
    a.append(int(temp[i])-1)

routetemp=[]
routetemp.append(0)
while True:
    if a[routetemp[-1]] in routetemp:
        roop=len(routetemp)-routetemp.index(a[routetemp[-1]])
        pre=routetemp.index(a[routetemp[-1]])
        break
    routetemp.append(a[routetemp[-1]])
#print(routetemp)
#print(a)
#print(roop)
#print(pre)
num=(k-pre)%roop
#print(num)
print(routetemp[pre+num]+1)
"""