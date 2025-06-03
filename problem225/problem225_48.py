import sys

def ISI(): return map(int, sys.stdin.readline().rstrip().split())

h, a =ISI()
print((h+a-1)//a)