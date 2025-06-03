
import itertools

n=int(input())
list1=list(map(int,input().split()))

q=int(input())
list2=list(map(int,input().split()))

sum1=set()

for i in range(1,n+1):
	x=list(itertools.combinations(list1,i))
	for j in x:
		sum1.add(sum(j))
		
		
for i in list2:
	if i in sum1:
		print("yes")
	else:
		print("no")
