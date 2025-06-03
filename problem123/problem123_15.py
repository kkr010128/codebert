import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
a = LI()

b = 0
for i in range(N):
    b ^= a[i]

print(*[b^a[i] for i in range(N)])
