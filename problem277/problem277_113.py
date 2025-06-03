import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  h,w,k=LI()
  field=[list(S()) for _ in range(h)]
  ans=[[0]*w for _ in range(h)]

  l=[]
  f=False
  y1=0
  x1=0
  for i in range(h):
    for j in range(w):
      if field[i][j]=='#':
        if f:
          l.append([y1,x1,i-1,w-1])
          y1=i
          x1=0
        f=True
        break
  l.append([y1,x1,h-1,w-1])
  # print(l)

  l2=[]
  while len(l)>0:
    y1,x1,y2,x2=l.pop()
    st=0
    f=False
    for j in range(x1,x2+1):
      for i in range(y1,y2+1):
        if field[i][j]=='#':
          if f:
            l2.append([y1,st,y2,j-1])
            st=j
          f=True
          break
    l2.append([y1,st,y2,x2])

  cnt=1
  while len(l2)>0:
    y1,x1,y2,x2=l2.pop()
    for i in range(y1,y2+1):
      for j in range(x1,x2+1):
        ans[i][j]=cnt
    cnt+=1

  for x in ans:
    print(' '.join([str(y) for y in x]))

main()
# print(main())
