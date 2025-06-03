A,B,C=map(int,input().split())
K=int(input())
i=0
while i<K:
    if A>=B:
        i+=1
        B*=2
    else:
        break
while i<K:
    if B>=C:
        i+=1
        C*=2
    else:
        break

print('YNeos'[(A>=B)or(B>=C)::2])