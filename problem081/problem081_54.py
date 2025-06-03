d=input()
arr = [int(i) for i in d.split()]

t1 = arr[0]/arr[-1]
if t1<= arr[1]:
  print("Yes")
else:
  print("No")
