(L,R,d) = map(int, input().split())
out=int(R/d)-int(L/d)+1
if ( L%d == 0):
  print (out)
else:
  print(out-1)