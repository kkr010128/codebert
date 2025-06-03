a , b , k  = map(int,input().split())
if k <= a:
  answer = ( a - k , b)
else:
  answer = (0 , max(0 , a + b -k))
print(*answer)