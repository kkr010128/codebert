n=int(input())
a=list(map(int,input().split()))
aa=[[1+i,x] for i,x in enumerate(a)]
aa.sort(key=lambda x:x[1])
aaa=[str(x[0]) for x in aa]
print(' '.join(aaa))