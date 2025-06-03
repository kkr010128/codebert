n=int(input())
R=[]
for i in range(n) :
    x,l=map(int,input().split())
    R.append([x+l,x-l])          #[右,左]
R.sort()                         #右側で小さい順からソート

def solve() :
    t,ans=-1000000000,0
    for i in range(n) :
        if R[i][1]>=t :
            ans+=1
            t=R[i][0]
    return ans

print(solve())