import sys
input=sys.stdin.readline
from itertools import accumulate
def main():
  n,k=map(int,input().split())
  a=list(map(int,input().split()))
  k=k if k<50 else 50
  for _ in range(k):
    b=[0]*(n+1)
    for i in range(n):
      ai=a[i]
      l,r=i-ai,i+ai+1
      l=0 if l<0 else l
      r=n if r>n else r
      b[l]+=1
      b[r]-=1
    b=tuple(accumulate(b))[:-1]
    a=b
    if min(set(b))==n:
      break
  print(*a)
if __name__ == '__main__':
  main()