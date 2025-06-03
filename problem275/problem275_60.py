x=list(map(int, input().split()))
t=0
if x[0]<4:
	t=t+((4-x[0])*100000)
if x[1]<4:
	t=t+((4-x[1])*100000)
if x[0]==1 and x[1]==1:
	t=t+400000
print(t)