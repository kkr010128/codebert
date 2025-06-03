from collections import deque

class SegmentTree():
    def __init__(self,n,ide_ele,merge_func,init_val):
        self.n=n
        self.ide_ele=ide_ele
        self.merge_func=merge_func
        self.val=[0 for i in range(1<<n)]
        self.merge=[0 for i in range(1<<n)]
        self.parent=[-1 for i in range(1<<n)]
        deq=deque([1<<(n-1)])
        res=[]
        while deq:
            v=deq.popleft()
            res.append(v)
            if not v&1:
                gap=(v&-v)//2
                self.parent[v-gap]=v
                deq.append(v-gap)
                self.parent[v+gap]=v
                deq.append(v+gap)
        for v in res[::-1]:
            if v-1<len(init_val):
                self.val[v-1]=init_val[v-1]
            self.merge[v-1]=self.val[v-1]
            if not v&1:
                gap=(v&-v)//2
                self.merge[v-1]=self.merge_func(self.merge[v-1],self.merge[v-gap-1],self.merge[v+gap-1])

    def update(self,id,x):
        self.val[id]=x
        pos=id+1
        while pos!=-1:
            if pos&1:
                self.merge[pos-1]=self.val[pos-1]
            else:
                gap=(pos&-pos)//2
                self.merge[pos-1]=self.merge_func(self.val[pos-1],self.merge[pos+gap-1],self.merge[pos-gap-1])
            pos=self.parent[pos]

    def cnt(self,k):
        lsb=(k)&(-k)
        return (lsb<<1)-1

    def lower_kth_merge(self,nd,k):
        res=self.ide_ele
        id=nd
        if k==-1:
            return res
        while True:
            if not id%2:
                gap=((id)&(-id))//2
                l=id-gap
                r=id+gap
                cnt=self.cnt(l)
                if cnt<k:
                    k-=cnt+1
                    res=self.merge_func(res,self.val[id-1],self.merge[l-1])
                    id=r
                elif cnt==k:
                    res=self.merge_func(res,self.val[id-1],self.merge[l-1])
                    return res
                else:
                    id=l
            else:
                res=self.merge_func(res,self.val[id-1])
                return res

    def upper_kth_merge(self,nd,k):
        res=self.ide_ele
        id=nd
        if k==-1:
            return res
        while True:
            if not id%2:
                gap=((id)&(-id))//2
                l=id-gap
                r=id+gap
                cnt=self.cnt(r)
                if cnt<k:
                    k-=cnt+1
                    res=self.merge_func(res,self.val[id-1],self.merge[r-1])
                    id=l
                elif cnt==k:
                    res=self.merge_func(res,self.val[id-1],self.merge[r-1])
                    return res
                else:
                    id=r
            else:
                res=self.merge_func(res,self.val[id-1])
                return res

    def query(self,l,r):
        id=1<<(self.n-1)
        while True:
            if id-1<l:
                id+=((id)&(-id))//2
            elif id-1>r:
                id-=((id)&(-id))//2
            else:
                res=self.val[id-1]
                if id%2:
                    return res
                gap=((id)&(-id))//2
                L,R=id-gap,id+gap
                #print(l,r,id,L,R)
                left=self.upper_kth_merge(L,id-1-l-1)
                right=self.lower_kth_merge(R,r-id)
                return self.merge_func(res,left,right)

ide_ele=0

def seg_func(*args):
    res=ide_ele
    for val in args:
        res|=val
    return res

def popcount(x):
    x = x - ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    return x & 0x0000007f

import sys

input=sys.stdin.readline

N=int(input())
S=input().rstrip()

init_val=[1<<(ord(S[i])-97) for i in range(N)]
test=SegmentTree(19,ide_ele,seg_func,init_val)

for _ in range(int(input())):
    t,l,r=input().split()
    t,l=int(t),int(l)
    if t==1:
        val=ord(r)-97
        test.update(l-1,1<<val)
    else:
        r=int(r)
        res=test.query(l-1,r-1)
        print(popcount(res))