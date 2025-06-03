num=int(input())
if num%1000==0:
  print(0)
else:
	print(1000-num%1000)