from math import sqrt
sigma=[]
while True:
	total=0
	nval=0
	n=int(input())
	if n==0:
		break

	score_list=map(float,raw_input().split(" "))

	for i in score_list:
		total+=i

	average=total/n

	for i in score_list:
		nval+=(average-i)**2
	val=nval/n
	sigma.append(sqrt(val))

for i in sigma:
	print i