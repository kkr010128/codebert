import sys

def ISI(): return map(int, sys.stdin.readline().rstrip().split())

n, r = ISI()
if n<10:
	r+=100*(10-n)
print(r)
