def main():
  n=int(input())
  s,t= list(map(str,input().split()))
  ans=""
  for i in range(0,n):
    ans+=s[i]+t[i]
  print(ans)

main()