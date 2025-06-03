n = int(raw_input())
minv = int(raw_input())
maxv = -1*10**9
  
for j in range( n-1 ):
  num = int( raw_input( ) )  
  diff = num - minv
  if maxv < diff:
    maxv = diff
  if num < minv:
    minv = num
  
print maxv