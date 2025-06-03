a=0
N=input()
l=len(N)
for i in range(l):
    if N[i]=='7':
        a=1
        break
if a==0:
    print('No')
else:
    print('Yes')