bit=[0 for i in xrange(200)]
n=int(raw_input().strip())
class dig:
    def __init__(self,val,id):
        self.val=val
        self.id=id
    def __gt__(self,other):
        return self.val<other.val


def sum(i):
    s=0
    i=int(i)
    while i>0:
        s+=bit[i]
        i-=i&(-i)
    return s
def add(i,x):
    i=int(i)
    while i<=n:
        bit[i]+=x
        i+=i&-i


def sort2(lst):
    lens=len(lst)
    sm=0
    for i in xrange(lens):
        for j in xrange(i+1,lens):
            if lst[i]>lst[j]:
                sm+=1
    return sm
lst=map(int,raw_input().strip().split())
vals=[]
lens=len(lst)
for i in xrange(lens):
    vals.append(dig(lst[i],i+1))
vals.sort()
ans=0
for i in vals:
    #print i.val,i.id
    ans+=sum(i.id)
    add(i.id,1)
ans=sort2(lst)
lst.sort()
print " ".join(str(pp) for pp in lst)
print ans


