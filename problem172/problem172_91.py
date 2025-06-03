a=int(input())
str_a=str(a)
list_a=list(str_a)
count=0
for i in range(0,len(list_a)):
	if(list_a[i]=='7'):
		count+=1
	else:
		count+=0
	
if(count>1 or count==1):
	print('Yes')
else:
	print('No')
