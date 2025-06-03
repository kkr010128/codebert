N,M=map(int, input().split())
SC=[list(map(int, input().split())) for _ in range(M)]
num=[-1]*N

for sc in SC:
	s,c=sc[0],sc[1]
	
	if s==1 and c==0 and N>1:
		print(-1)
		exit()
	elif num[s-1]==c or num[s-1]==-1:
		num[s-1]=c
	else:
		print(-1)
		exit()

if N==3:
	if num[0]==-1:
		num[0]=1
	if num[1]==-1:
		num[1]=0
	if num[2]==-1:
		num[2]=0
	print(num[0]*100+num[1]*10+num[2])
elif N==2:
	if num[0]==-1:
		num[0]=1
	if num[1]==-1:
		num[1]=0
	print(num[0]*10+num[1])
else:
	if num[0]==-1:
		num[0]=0
	print(num[0])