def main():
  import sys
  n,s,_,*t=sys.stdin.buffer.read().split()
  n=int(n)
  d=[0]*n+[1<<c-97for c in s]
  for i in range(n-1,0,-1):d[i]=d[i+i]|d[i-~i]
  for q,a,b in zip(*[iter(t)]*3):
    i,s=int(a)+n-1,0
    if q<b'2':
      d[i]=1<<b[0]-97
      while i>1:
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
    print(bin(s).count('1'),flush=False)
main()