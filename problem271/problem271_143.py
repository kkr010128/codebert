n=int(input())
a=input()

for i in a:
  if ord(i)+n<=90:
    print(chr(ord(i)+n),end='')
  else:
    print(chr(ord(i)+n-26),end='')
