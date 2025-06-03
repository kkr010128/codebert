from fractions import gcd
N, M = map(int, input().split())
S = list(map(int, input().split()))

temp = S[0]
cnt = 0
while temp%2 == 0:
    temp //= 2
    cnt += 1
temp = S[0]
for i in range(1, N):
    temp = temp*S[i]//gcd(temp, S[i])
    if S[i]%(2**cnt) == 1 or (S[i]//(2**cnt))%2 == 0:
        print(0)
        break
else:      
    if temp//2 > M:
        print(0)
    else:
        print((M-temp//2)//temp+1)