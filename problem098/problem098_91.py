import sys
input = sys.stdin.readline

N = int(input())
S = input()[:-1]
R = S.count('R')
accR = [0]

for Si in S:
    accR.append(accR[-1]+(1 if Si=='R' else 0))

ans = 10**18

for i in range(N+1):
    ans = min(ans, abs(i-R)+abs(i-accR[i]))

print(ans)