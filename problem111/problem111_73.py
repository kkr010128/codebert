import collections

n=int(input())
a= list(map(int, input().split()))
aa=list(set(a))
sortaa=sorted(aa,reverse=True)
c = collections.Counter(a)
comf=[]
for i in range(len(aa)):
    if i == 0:
        comf.extend([sortaa[i] for ii in range(2*c[sortaa[i]]-1)])
    else:
        comf.extend([sortaa[i] for ii in range(2*c[sortaa[i]])])

print(sum(comf[:n-1]))