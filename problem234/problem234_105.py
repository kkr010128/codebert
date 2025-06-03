import sys
import  math
from heapq import *
import fractions
from collections import defaultdict
stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

N=int(input())
n_l=[[0]*10 for i in range(10)]#col matu row sentou
for i in range(1,N+1):
    if(1<=i and i<10):
        n_l[i][i]+=1
    elif(10<i and i<10**2):
        n_l[i%10][i//10]+=1
    elif(10**2<i and i<10**3):
        n_l[i%10][i//100]+=1
    elif(10**3<i and i<10**4):
        n_l[i%10][i//1000]+=1
    elif(10**4<i and i<10**5):
        n_l[i%10][i//10000]+=1
    elif(10**5<i):
        n_l[i%10][i//100000]+=1
    

ans=0
for i in range(1,10):
    for k in range(1,10):
        if(i!=k):
            ans+=(n_l[i][k])*((n_l[k][i]))

for i in range(1,10):
    ans+=(n_l[i][i])*((n_l[i][i]))
print(ans)
