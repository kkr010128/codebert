n=int(input())
A=list(map(int,input().split()))
q=int(input())
M=list(map(int,input().split()))

pattern=[]

for i in range(2**n):
    s=0
    for j in range(n):
        if i >> j & 1:
            s+=A[j]
    pattern.append(s)
P=set(pattern)

for m in M:
    print('yes' if m in P else 'no')
