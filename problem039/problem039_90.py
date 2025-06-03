a,b,c=map(int, input().split())
0<=a<=100,0<=b<=100,0<=c<=100,
if a<b:
  if b<c:
    print('Yes')
  else:
    print('No')
else:
  print('No')
