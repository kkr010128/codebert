import sys
def ISI(): return map(int, sys.stdin.readline().rstrip().split())
a, b = ISI()
if a<2*b:print(0)
else:print(a-2*b)