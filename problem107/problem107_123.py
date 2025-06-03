N=int(input())
X=input()
popcount=X.count('1')
bi1=[]
bi0=[]
Xnum1 = 0
Xnum0 = 0
if popcount != 1:
    for i in range(N):
        if i==0: bi1.append(1)
        else: bi1.append(bi1[i-1]*2%(popcount-1))
        Xnum1 = (Xnum1 + int(X[N-i-1])*bi1[i])%(popcount-1)
for i in range(N):
    if i==0: bi0.append(1)
    else: bi0.append(bi0[i-1]*2%(popcount+1))
    Xnum0 = (Xnum0 + int(X[N-i-1])*bi0[i])%(popcount+1)
for i in range(N):
    if popcount==1 and X[i]=='1':
        print(0)
        continue
    if X[i]=='1':
        Xi = (Xnum1 - bi1[N-i-1])%(popcount-1)
    else:
        Xi = (Xnum0 + bi0[N-i-1])%(popcount+1)
    ans = 1
    while Xi!=0:
        Xi = Xi % bin(Xi).count('1')
        ans += 1
    print(ans)