n = int(input())
al = 26
alf='abcdefghijklmnopqrstuvwxyz'
na = ''
while n >26:
  na = alf[(n-1)%al]+na
  n = (n-1)//al

na = alf[(n-1)%al]+na
print(na)