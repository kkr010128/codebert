if __name__ == '__main__':
  def linearSearch(t):
    S.append(t)
    #print(S)
    i=0
    while S[i]!=t:
      i+=1
    del S[n]
    return 1 if i!=n else 0

  n=int(input())
  S=list(map(int,input().split()))
  q=int(input())
  T=set(map(int,input().split()))

  ans=0
  for t in T:
    ans+=linearSearch(t)
    #print(t,ans)
  print(ans)

