N = int(input())
P = []
for i in range(N):
    s = [int(i) for i in input().split()]
    P.append(s)
L = []
for i in range(N-1):
    for j in range(i+1, N):
        l = (P[i][0] - P[j][0])**2 + (P[i][1] - P[j][1])**2
        L.append(l**0.5)
S = sum(L)
print(2*S/N)