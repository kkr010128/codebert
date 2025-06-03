def main():
  n = int(input())
  a = list(map(int,input().split()))
  flg=0
  for i in range(0,n):
    if a[i]%2==0 :
      if a[i]%3!=0 and a[i]%5!=0 :
        flg=1
  if flg==0:
    print("APPROVED")
  else:
    print("DENIED")
main()