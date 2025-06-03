t=int(input())
count = 0
flag = False
for test in range(t):
    a,b = map(int,input().split())
    if a==b:
    	count+=1
    	if count==3:
    		flag=True
    else:
    	count=0

if flag:
	print("Yes")
else:
	print("No")