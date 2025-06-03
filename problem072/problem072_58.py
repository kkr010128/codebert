def input_array():
	return list(map(int,input().split()))
  
n=int(input())
D=[input_array() for i in range(n)]

count=0
for d in D:
	if d[0]==d[1]:
		count+=1
	else:
		count=0

	if count==3:
		break
if count==3:
	print("Yes")
else:
	print("No")