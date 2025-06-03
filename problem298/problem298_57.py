def main():
  n,k= list(map(int,input().split()))
  h= list(map(int,input().split()))
  ans=0
  for i in range(0,n):
    if h[i]>=k:
      ans+=1
  print(ans)

main()