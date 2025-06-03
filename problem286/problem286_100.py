import sys
def ISI(): return map(int, sys.stdin.readline().rstrip().split())

a, b=ISI()
if a>9 or b>9:print(-1)
else:print(a*b)
