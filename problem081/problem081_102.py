
#入力:N,M(int:整数)
def input2():
	return map(int,input().split())
  
d,t,s=input2()
if d/s >t:
	print("No")
else:
	print("Yes")