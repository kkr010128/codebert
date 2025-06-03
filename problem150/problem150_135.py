N,K = map(int, input().split())
A = list(map(int, input().split()))
k = K.bit_length()
dv = [[0]*N for _ in range(k)]
dv[0] = [a-1 for a in A]
for turn in range(1,k):
    for town in range(N):
        dv[turn][town] = dv[turn-1][dv[turn-1][town]]

a = 0
for i in range(k):
    if (K>>i)&1:
        a = dv[i][a]
        
print(a+1)