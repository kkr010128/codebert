def main():
  x,y = list(map(int,input().split()))
  ans=0
  for i in range(0,x+1):
    if 2*i+4*(x-i)==y:
      ans=1
  if ans==1:
    print("Yes")
  else:
    print("No")
main()