S = input()
array = list(S)
N = len(array)
a = (N-2)//2
b = (N+2)//2
if array[0:a+1] == array[b:N]:
  print('Yes')
else:
  print('No')