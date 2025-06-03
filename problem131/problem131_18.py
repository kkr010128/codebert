import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
a, v = M() # おに
b, w = M() # にげる
t = I()
ans = 'NO'
if v-w > 0:
    b_hiku_a = abs(b - a)
    v_hiku_w = v - w
    if b_hiku_a <= t * (v-w):
        ans = 'YES'
print(ans)