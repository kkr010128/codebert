import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
d = LI()

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        ans += d[i]*d[j]

print(ans)