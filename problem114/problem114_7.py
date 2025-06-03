import random

D = int(input())
C = list(map(int,input().split()))
S = []
for i in range(D):
    S.append(list(map(int,input().split())))
t = []
for i in range(D):
    #t.append(int(random.uniform(0,26)))
    t.append(int(input()))
lastds = [0]*26
ans = 0
satisfaction = 0
#initial
for d in range(D):
    lastds[t[d]-1] = d+1
    satisfaction += S[d][t[d]-1]
    for i in range(26):
        satisfaction -= C[i] * (d+1-lastds[i])
    print(satisfaction)