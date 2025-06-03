d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]
t = []
for _ in range(d):
    t.append(int(input()))

cl = sum(c)
D = [0]*26
sas = 0

for i in range(d):
    for j in range(26):
      D[j] += 1
    T = t[i] 
    S = s[i][T-1]
    C = c[T-1]
    D[T-1] = 0
    dc = 0
    for j in range(26):
      dc += D[j]*c[j]
    sas += S - dc
    print(sas)