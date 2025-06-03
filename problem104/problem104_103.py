import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

l,r,d = map(int,readline().split())

a = (l-1)//d
b = r//d

print(b-a)