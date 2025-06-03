import sys
input = sys.stdin.readline
from collections import *

S = input()[:-1]
K = int(input())

if S==S[0]*len(S):
    print(len(S)*K//2)
    exit()
    
l = []
cnt = 1

for i in range(len(S)-1):
    if S[i]!=S[i+1]:
        l.append((S[i], cnt))
        cnt = 1
    else:
        cnt += 1
    
l.append((S[-1], cnt))

if K==1 or l[0][0]!=l[-1][0]:
    ans = 0
    
    for _, c in l:
        ans += c//2*K
else:
    ans = (l[0][1]+l[-1][1])//2*(K-1)
    ans += l[0][1]//2
    ans += l[-1][1]//2
    
    for _, c in l[1:-1]:
        ans += c//2*K

print(ans)