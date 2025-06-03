import sys
from itertools import accumulate
 
read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines

import bisect

n,m=map(int,input().split())
A=list(map(int,input().split()))
A.sort()

def hand(x):
  cnt=0
  for i in range(n):
    k=n-bisect.bisect_left(A,x-A[-i-1])
    if k==0:
      break
    cnt+=k
    if cnt>=m:
      break
  return cnt

def main():
  l=0
  h=2*10**5+1
  mid=(l+h)//2
  
  while l+1<h:
    mid=(l+h)//2
    if hand(mid)<m:
      h=mid
    else:
      l=mid
  
  B = list(accumulate(A[::-1]))[::-1]

  ans=0
  cnt=0
  
  
  for i in range(n):
    index=bisect.bisect_left(A,l-A[-i-1]+1)
    if n==index:
      break
    else:
      ans+=(n-index)*A[-i-1]+B[index]
      cnt+=(n-index)
  
  ans+=(m-cnt)*l
  print(ans)

if __name__ == "__main__":
	main()
  

  
  