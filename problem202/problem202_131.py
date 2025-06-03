import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

n, a, b = inm()
if a == 0:
    print(0)
elif n >= a+b:
    print(n//(a+b) * a + min(a, n % (a+b)))
else:
    print(min(n, a))