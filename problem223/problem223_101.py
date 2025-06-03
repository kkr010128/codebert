import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())
def NIJIGEN(H): return [list(input()) for i in range(H)]
N,M=MAP()
L=LIST()
maxa=-(10**10)
sums=sum(L[:M])
maxa=max(maxa,sums)
for i in range(N-M):
  sums=sums-L[i]+L[i+M]
  maxa=max(maxa,sums)
print((maxa+M)/2)