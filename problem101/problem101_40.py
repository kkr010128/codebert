A,B,C=map(int,input().split())
K=int(input())

for i in range(K):
    if A>=B:
        B=2*B
    elif B>=C:
        C=2*C
    if A<B and B<C:
        print('Yes')
        break
else:
    print('No')