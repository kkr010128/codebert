N = int(input())

for i in range(10):
  pay = (i + 1) * 1000
  if(pay >= N):
    break

if(pay < N):
  print("たりません")
else:
	print(pay - N)