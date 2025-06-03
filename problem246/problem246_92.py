import itertools
#h,w=map(int,input().split())
#S=[list(map(int,input().split())) for _ in range(h)]
n=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
num=0
numlist=[i for i in range(1,n+1)]
pall=list(itertools.permutations(numlist))
for pp in pall:
    if P==list(pp):
        pnum=num
    if Q==list(pp):
        qnum=num
    num+=1
print(abs(pnum-qnum))