import itertools

#a=itertools.product([0,1],repeat=N)

N = int(input())
AAA = [[] for i in range(N)]

for i in range(N):
    A = int(input())
    for j in range(A):
        AAA[i].append([int(k) for k in input().split()])


for ifkind in itertools.product([1,0],repeat=N):
    consistent = True
    for i,A in enumerate(AAA):
        if ifkind[i]==1:
            for x,y in A:
                x=x-1
                if ifkind[x]!=y:
                    consistent = False
    if consistent==True:
        print(sum(ifkind))
        break
