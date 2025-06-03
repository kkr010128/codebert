def main():
  import sys
  input=sys.stdin.buffer.readline
  n=int(input())
  d=[0]*n+[1<<c-97for c in input()[:n]]
  for i in range(n-1,0,-1):d[i]=d[i+i]|d[i-~i]
  r=[]
  for _ in range(int(input())):
    q,a,b=input().split()
    i,s=int(a)+n-1,0
    if q<b'2':
      d[i]=1<<b[0]-97
      while i:
        i//=2
        d[i]=d[i+i]|d[i-~i]
      continue
    j=int(b)+n
    while i<j:
      if i&1:
        s|=d[i]
        i+=1
      if j&1:
        j-=1
        s|=d[j]
      i//=2
      j//=2
    r+=bin(s).count('1'),
  print(' '.join(map(str,r)))
main()