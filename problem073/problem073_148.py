n = int(input())
i,j=1,1
count=0

x = i*j
cc = n-x

while cc>=1:

	cnt=0
	while 1:
		p = i*j
		c = n - p
		if c>=1:
			#print(i,":",j,":",c)
			j=j+1
			cnt+=1
		else:
			j=i
			break

	count=count+((cnt*2)-1)

	i=i+1
	j=j+1

	x = i*j
	cc = n-x


print(count)