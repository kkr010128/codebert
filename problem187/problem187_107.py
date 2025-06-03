N,X,Y=map(int,input().split())
#i<X<Y<j
#このときはX->を通るほうが良い
#X<=i<j<=Y
#このときはループのどちらかを通れば良い
#X<=i<=Y<j
#このときはiとYの最短距離+Yとjの最短距離
#i<X<=j<=Y
#同上
#i<j<X
#パスは1通りしか無い
def dist(i,j):
    if i>j:
        return dist(j,i)
    if i==j:
        return 0
    if i<X:
        if j<X:
            return j-i
        if X<=j and j<=Y:
            return min(j-i,(X-i)+1+(Y-j))
        if Y<j:
            return (X-i)+1+(j-Y)
    if X<=i and i<=Y:
        if j<=Y:
            return min(j-i,(i-X)+1+(Y-j))
        if Y<j:
            return min((i-X)+1+(j-Y),j-i)
    if Y<i:
        return (j-i)
ans=[0 for i in range(N)]
for i in range(1,N+1):
    for j in range(i+1,N+1):
        ans[dist(i,j)]+=1
for k in range(1,N):
    print(ans[k])