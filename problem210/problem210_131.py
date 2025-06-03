import bisect

N=int(input())
S=list(input())
Q=int(input())

alphabet="abcdefghijklmnopqrstuvwxyz"
bag={l:[] for l in alphabet}
for i in range(N):
    bag[S[i]].append(i+1)
#print(bag)

for i in range(Q):
    Type,a,b=input().split()
    if Type=='1':
        a=int(a)
        if S[a-1]!=b:
            bag[S[a-1]].remove(a)
            S[a-1]=b
            bisect.insort(bag[b],a)
    else:
        cnt=0
        a,b=int(a),int(b)
        for l in alphabet:
            bl=len(bag[l])
            if bl>0:
                left=bisect.bisect_left(bag[l],a)
                if left!=bl and bag[l][left]<=b:
                        cnt+=1
        print(cnt)