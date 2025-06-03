N = int(input())
flg = 'No'
for i in range(1,10):
  for j in range(1, 10):
    if N == i*j:
      flg = 'Yes'
print(flg)