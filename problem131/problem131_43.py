ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a,v=nm()
b,w=nm()
t=ni()

d=abs(a-b)
d2=(v-w)*t

if(d<=d2):
  print('YES')
else:
  print('NO')
