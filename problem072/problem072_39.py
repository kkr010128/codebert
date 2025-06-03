N = int(input())
d_ls=[]
for vakawkawelkn in range(N):
	D1,D2=map(int, input().split())
	if D1==D2:
		d_ls+=[1]
	else:
		d_ls+=[0]

flag=0
for i in range(N-2):
	if d_ls[i]*d_ls[i+1]*d_ls[i+2]==1:
		flag=1


if flag==0:
	print("No")
else:
	print("Yes")


# 2darray [[0] * 4 for i in range(3)]
# import itertools