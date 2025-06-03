import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())
def NIJIGEN(H): return [list(input()) for i in range(H)]
N,M=MAP()
H=LIST()
L=[[0] for i in range(N)]
for i in range(M):
  a,b=MAP()
  a-=1
  b-=1
  L[a].append(H[b])
  L[b].append(H[a])
ans=0
for i in range(N):
  if max(L[i])<H[i]:
    ans+=1
print(ans)