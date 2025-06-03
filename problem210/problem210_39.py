def main():
  import sys
  b=sys.stdin.buffer
  input=b.readline
  n=int(input())
  d=[set()for _ in range(n)]+[{c}for c in input()]
  for i in range(n-1,0,-1):d[i]=d[i+i]|d[i-~i]
  r=[]
  add=r.append
  input()
  for q,a,b in zip(*[iter(b.read().split())]*3):
    i=int(a)+n-1
    if q<b'2':
      d[i]={b[0]}
      while i:
        i>>=1
        d[i]=d[i+i]|d[i-~i]
      continue
    j=int(b)+n
    s=set()
    while i<j:
      if i&1:
        s|=d[i]
        i+=1
      if j&1:
        j-=1
        s|=d[j]
      i>>=1
      j>>=1
    add(len(s))
  print(' '.join(map(str,r)))
main()