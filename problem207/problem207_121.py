a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a3=list(map(int,input().split()))

n=int(input())
for i in range (n):
  num=int(input())
  if num in a1:
  	a1[a1.index(num)]='O'
  if num in a2:
  	a2[a2.index(num)]='O'
  if num in a3:
  	a3[a3.index(num)]='O'
if a1[0] == 'O' and a1[1] == 'O' and a1[2] == 'O':
  print('Yes')
elif a2[0] == 'O' and a2[1] == 'O' and a2[2] == 'O':
  print('Yes')
elif a3[0] == 'O' and a3[1] == 'O' and a3[2] == 'O':
  print('Yes')
elif a1[0] == 'O' and a2[0] == 'O' and a3[0] == 'O':
  print('Yes')
elif a1[1] == 'O' and a2[1] == 'O' and a3[1] == 'O':
  print('Yes')
elif a1[2] == 'O' and a2[2] == 'O' and a3[2] == 'O':
  print('Yes')
elif a1[0] == 'O' and a2[1] == 'O' and a3[2] == 'O':
  print('Yes')
elif a1[2] == 'O' and a2[1] == 'O' and a3[0] == 'O':
  print('Yes')
else:
  print('No')