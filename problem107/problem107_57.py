N=int(input())
X=input()
c=X.count('1')
r1=int(X,2)%(c-1) if c>1 else 0
r2=int(X,2)%(c+1)
d=[0]*(N+1)
for i in range(N):
    d[i+1]=d[(i+1)%bin(i+1).count('1')]+1
for i in range(N):
    if X[i]=='0':
        n=(r2+pow(2,N-i-1,c+1))%(c+1)
    else:
        if c==1:
            print(0)
            continue
        n=(r1-pow(2,N-i-1,c-1))%(c-1)
    print(d[n]+1)