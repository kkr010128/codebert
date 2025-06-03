import copy

def countKuro( t,p1,p2 ):
    count=0
    for i in range(h):
      if p1 & (1<<i) :
        for j in range(w):
            if p2 & (1<<j) :
                if t[i][j]=="#":
                    count+=1
    return count


h,w,k=map(int, input().split())
s=[]
for i in range(h):
    s.append( input() )

t=copy.copy(s)
ans=0
for i in range(1<<h):
    for j in range(1<<w):
        # print(i,j, countKuro(s,i,j))
        if k==countKuro(s, i,j):
            ans+=1
print(ans)
