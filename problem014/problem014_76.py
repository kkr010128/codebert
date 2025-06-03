def bubble(A,N):
	flag=1
	cnt=0
	while flag==1:
		flag=0
		for j in range(1,N):
			if A[j]<A[j-1]:
				k=A[j-1]
				A[j-1]=A[j]
				A[j]=k
				flag=1
				cnt+=1
	return A,cnt
n=int(raw_input())			
list=map(int,raw_input().split())
list,cnt=bubble(list,n)
for x in list:
	print x,
print
print cnt,