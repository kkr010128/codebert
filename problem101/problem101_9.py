A,B,C=map(int,input().split())
K=int(input())
D=[]
for i in range(K):
    for j in range(K-i):
        if A*(2**i)<B*(2**j) and B*(2**j)<C*(2**(K-i-j)):
            D.append('Yes')
        else:
            D.append('No')
if ('Yes' in D)==True:
    print('Yes')
else:
    print('No')