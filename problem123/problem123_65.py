import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
N = I()
a = LI()
xor = 0
for x in a:
    xor ^= x
for x in a:
    print(xor^x,end=' ')
print()
