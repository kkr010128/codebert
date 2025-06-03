n = int(input())
k = 1000000007
if n == 1:
  print(0)
  
else:
  print(((10**n)%k - (2* 9**n)%k+(8**n)%k)%k)