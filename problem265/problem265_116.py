n=int(input())
for i in range(46298):
  if int(i*1.08)==n:
    print(i)
    break
else:
  print(":(")