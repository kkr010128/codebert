a,b,c=map(int,input().split())
K=int(input())

# B > A
# C > B
import sys
for i in range(K+1):
    A=a
    B=b*(2**i)
    C=c*(2**(K-i))
    #print(i,K-i,A,B,C)
    if B>A and C>B:
        print('Yes')
        sys.exit()
else:
    print('No')