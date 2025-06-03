n=int(input())

if n==0 or n==1:
  print(0)

else:
  print((10**n - (2*(9**n)-8**n))%(10**9+7))