a,b,k = map(int, input().split())
if k > a and k >= a+b:
  print( 0 , 0 )
elif k < a :
  print(a-k , b)
elif k == a:
  print(0 , b)
elif k>a and k < a+b:
  print(0 , b-(k-a))

