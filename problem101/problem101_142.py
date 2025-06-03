import sys
import  math
import fractions
from collections import defaultdict
stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

A,B,C=nm()
K=int(input())

count=0
while(B<=A):
    B*=2
    count+=1
while(C<=B):
    C*=2
    count+=1

print('No' if K<count else 'Yes')



    
