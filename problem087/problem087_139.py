#176-B

N = input()
sum = 0
for i in range(1,len(N)+1):
  sum += int(N[-i])

if int(sum) % 9 == 0:
  print('Yes')
else:
  print('No')
