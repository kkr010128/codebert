def main():
  n,a,b = list(map(int,input().split()))
  ans=0
  count=int(n/(a+b))
  ans+=count*a
  amari=n-count*(a+b)
  if amari <= a:
    ans+=amari
  else:
    ans+=a
  print(ans)
main()