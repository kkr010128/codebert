list=list(map(int,input().split()))

if list[0]%(list[1]+list[2])==0:
	print((list[0]//(list[1]+list[2]))*list[1])
elif list[0]%(list[1]+list[2])<=list[1]:
	print((list[0]//(list[1]+list[2]))*list[1]+list[0]%(list[1]+list[2]))
else:
	print(list[0]//(list[1]+list[2])*list[1]+list[1])