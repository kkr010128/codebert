from collections import Counter

N, P = map(int, input().split())
S = input()

sum = 0
if P == 2 or P == 5:
    for i in range(N):
        if int(S[i]) % P == 0:
            sum += i+1
    print(sum)
    exit()

m = []
t = 1
q = 0
for i in range(N,0,-1):
    q = ((int(S[i-1]) % P) * t + q) % P
    m.append(q)
    t = (10 * t) % P
    
mc = Counter(m)

for v in mc.values():
    if v > 1:
        sum += v*(v-1)//2

sum += mc[0]

print(sum)