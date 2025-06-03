def test():
  n=int(input())
  A=list(map(int,input().split()))
  a=1

  if (0 in A):
    print("0")
    return

  for i in A:
    a*=i
    if a > 10**18:
      print("-1")
      return
  print(a) 
test()