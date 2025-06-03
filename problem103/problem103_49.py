n=int(input())
A=list(map(int, input().split()))

stock=0
money=1000
d=-1
for i in range(len(A)-1):
	if A[i+1]-A[i]>0 and d==-1:
		'''kau'''
		stock=money//A[i]
		money=money%A[i]
		d=1
	elif A[i+1]-A[i]<0 and d==1:
		'''uru'''
		money+=A[i]*stock
		stock=0
		d=-1
	#print(i,money,stock)
if stock!=0:
	money += A[-1]*stock
	stock=0
print(money)
