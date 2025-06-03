import itertools
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

l = [int(x) for x in range(1,n+1)]
i = 0
p_i = 0
q_i = 0
for v in itertools.permutations(l, len(l)):
    i += 1
    if p==list(v):
        p_i = i
        #print(list(v))
    if q==list(v):
        q_i = i
        #print(i,list(v))
print(abs(p_i-q_i))
