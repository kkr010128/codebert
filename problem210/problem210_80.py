import bisect

n=int(input())
s=list(input())

#アルファベットの各文字に対してからのリストを持つ辞書
alpha={chr(i):[] for i in range(97,123)}

#alpha[c]で各文字ごとに出現場所をソートして保管
for i,c in enumerate(s):
    bisect.insort(alpha[c],i+1)

for i in range(int(input())):
    p,q,r=input().split()
    if p=='1':
        q=int(q)
        b=s[q-1]
        if b!=r:
            alpha[b].pop(bisect.bisect_left(alpha[b],q))
            bisect.insort(alpha[r],q)
            s[q-1]=r
    else:
        count=0
        for l in alpha.values():
            pos=bisect.bisect_left(l,int(q))
            if pos<len(l) and l[pos]<=int(r):
                count+=1
        print(count)
