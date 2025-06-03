import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

H1, M1, H2, M2, K = mapint()
if M2>=M1:
    minutes = (H2-H1)*60
    minutes += M2-M1
else:
    minutes = (H2-H1-1)*60
    minutes += M2-M1+60
print(max(0, minutes-K))
