def main():
  s=input()
  ans=0
  for i in range(0,int(len(s)/2)):
    if s[i]!=s[-1*(i+1)]:
      ans+=1
  print(ans)

main()