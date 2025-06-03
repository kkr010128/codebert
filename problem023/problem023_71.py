n=int(input())
A=set()
for i in range(n):
     x,y=input().split()
     if x == 'insert':
         A.add(y)
     else:
         print('yes'*(y in A)or'no')
