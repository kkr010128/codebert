import sys
readline = sys.stdin.readline

a,b,c,K = map(int,readline().split())

print(min(a,K) - max(K - (a + b),0))