N=int(raw_input())
max=(-1)*(10**9)
x1=input()
min=x1

for i in range(N-1):
  x=int(raw_input())

  if max < x-min:
    max=x-min
  if min>x:
    min=x
print max