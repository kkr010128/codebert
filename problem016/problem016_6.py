n=int(input())
a=list(map(str,input().split()))

ab=a[:]
flg=True
i=0
while flg:
    flg=False
    for j in range(n-1,i,-1):
        if ab[j][1]<ab[j-1][1]:
            ab[j],ab[j-1]=ab[j-1],ab[j]
            flg=True
    i+=1
print(' '.join(map(str,ab)))
print('Stable')

ac=a[:]
for i in range(n):
    minj=i
    for j in range(i,n):
        if ac[j][1]<ac[minj][1]:
            j,minj=minj,j
    if i!=minj:
        ac[i],ac[minj]=ac[minj],ac[i]
print(' '.join(map(str,ac)))

if ab==ac:
    print('Stable')
else:
    print('Not stable')
