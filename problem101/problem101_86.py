A,B,C=map(int,input().split())
K=int(input())
count=0
if B<=A:    
    while B<=A:
        B*=2
        count+=1
if count>K:
    print('No')
else:
    C*=2**(K-count)
    if C>B:
        print('Yes')
    else:
        print('No')