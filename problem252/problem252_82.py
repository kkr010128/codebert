import sys
 
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
    p=x-A[i]
    cnt+=n-bisect.bisect_left(A,p)
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
  
  B=A[::-1]
  
  for i in range(n-1):
    B[i+1]+=B[i]
  
  B=B[::-1]
  
  ans=0
  cnt=0
  
  
  for i in range(n):
    y=l-A[i]+1
    index=bisect.bisect_left(A,y)
    if n==index:
      continue
    else:
      ans+=(n-index)*A[i]+B[index]
      cnt+=(n-index)
  
  ans+=(m-cnt)*l
  print(ans)

if __name__ == "__main__":
	main()
  

  
  