n,k=map(int,input().split())
amari=n%k

if amari>k:
  print(k)
else:
  print(min(amari,abs(amari-k)))