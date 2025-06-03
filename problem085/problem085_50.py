import math

N = int(input())
A = list(map(int, input().split()))

inf = int(1e6+5)
C = [0]*inf

for a in A:
    C[a] += 1

pa = True
se = True
for i in range(2, inf):
    cnt = 0
    cnt += sum(C[i::i])
    if cnt > 1:
        pa = False
    if cnt == N:
        se = False
        
if pa:
    print("pairwise coprime")
elif se:
    print("setwise coprime")
else:
    print("not coprime")
