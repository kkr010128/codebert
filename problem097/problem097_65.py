k=int(input())
if k%7==0:
    k = 9*k//7
else:
    k *= 9
f=10%k
r = -1
for i in range(10**7):
    if f==1:
        r = i+1
        break
    else:
        f = f*10%k
print(r)