N,K=map(int,input().split())
lst=list(map(int,input().split()))
if K>=N:
    print(0)
else:
  lst.sort()
  s=sum(lst[0:N-K])
  print(s)