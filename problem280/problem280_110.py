import itertools,math
N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())
seq=[]
for i in range(N):
    seq.append(i)
    
l=list(itertools.permutations(seq))

num=0
for i in l:
    for u in range(1,len(i)):
        num+=math.sqrt((x[i[u-1]]-x[i[u]])**2+(y[i[u-1]]-y[i[u]])**2)
print(num/len(l))    