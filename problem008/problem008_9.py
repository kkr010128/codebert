#16D8101014F KurumeRyunosuke 2018/6/20

n=int(input())
ls=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
	tmp=input().split()
	for j in range(int(tmp[1])):
		ls[i][int(tmp[j+2])-1]=1

"""
for i in range(n):
    for j in range(n):
        if(j!=n-1):
            print(int(ls[i][j]), end=' ')
        else:
            print(int(ls[i][j]))
"""
stuck=[0]
count=1
d=[0 for i in range(n)]
f=[0 for i in range(n)]
d[0]=count
for i in range(n):
	ls[i][0]=0

while True:
	count+=1
	p=0
	#print("S",d)
	for i in range(n):
		if ls[stuck[len(stuck)-1]][i] is not 0:
			ls[stuck[len(stuck)-1]][i]=0
			p=1
			#print(stuck)
			stuck.append(i)
			d[stuck[len(stuck)-1]]=count
			break
	#print(d,"**")
	if p is 1:
		for i in range(n):
			ls[i][stuck[len(stuck)-1]]=0

	if p is 0:
		#print("//",count)
		a=stuck.pop()
		f[a]=count
		for i in range(n):
			ls[a][i]=0
	#print(d,"¥¥¥")
	if len(stuck) is 0:
		t=0
		for i in range(n):
			for j in range(n):
				if ls[i][j] is not 0 and t is 0:
					count+=1
					stuck.append(i)
					d[stuck[len(stuck)-1]]=count
					#print(i,"***")
					t=1
					
		if t is 0:
			break
		#print("break")
	#print("G",d,f,count)

for i in range(n):
	print(i+1,d[i],f[i])

