def func(x):
  if x==1:
    return 1
  else:
    if x%2==1:
      return func(x-1)
    else:
      return 2*func(x/2)+1
n=int(input())
print(func(n))