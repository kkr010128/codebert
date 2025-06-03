a='abcdefghijklmnopqrstuvwxyz'
N=int(input())
name=''
while N>0:
  N-=1
  name+=a[N%26]
  N//=26
print(name[::-1])