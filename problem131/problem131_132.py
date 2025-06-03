a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
gap=abs(a-b) 
if v>w:
  c=gap/(v-w)
  if t>=c:
    print('YES')
  else:
    print('NO')
else:
  print('NO')