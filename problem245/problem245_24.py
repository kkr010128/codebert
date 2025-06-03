import sys

def I(): return int(sys.stdin.readline().rstrip())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
S = LS2()

ans = 0
for i in range(N-2):
    if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
        ans += 1

print(ans)