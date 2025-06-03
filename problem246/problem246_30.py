import itertools
n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
target= range(1,n+1)
p_len=0
q_len=0
for i,v in enumerate(itertools.permutations(target,n)):
    tmp=list(v)
    if p==tmp:
        p_len=i
    if q==tmp:
        q_len=i
print(abs(p_len-q_len))