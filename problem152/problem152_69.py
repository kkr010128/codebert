from itertools import accumulate,chain
n,*s=open(0).read().split()
t=[2*i.count("(")-len(i) for i in s]
st=[[min(accumulate(s_,lambda a,b: a+(1 if b=="(" else -1),initial=0)),t_] for s_,t_ in zip(s,t)]
now=0
for c,d in chain(sorted([x for x in st if x[1]>=0])[::-1],sorted([x for x in st if x[1]<0],key=lambda z:z[1]-z[0])[::-1]):
    if now+c<0:
        print("No");break
    now+=d
else:
    print("No" if now else "Yes")