n=int(input())

if n==0 or n==1 or n==2:
  print(0)
elif n==3:
  print(1)
elif n%2==1:#奇数
  print(int(n/2))
elif n%2!=1:#偶数
  print(int(n/2)-1)