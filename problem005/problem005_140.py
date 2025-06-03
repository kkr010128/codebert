ans=[]
while True:
	try:
		k,l=list(map(int,input().split(" ")))
		init_k=k
		init_l=l
#
		while True:
			if k%l==0:
				gcd=l
				tmp_1=init_k/gcd
				tmp_2=init_l/gcd
				lcm=gcd*tmp_1*tmp_2
				break
			else:
				tmp=k%l
				k=l
				l=tmp
		gcd=int(gcd)
		lcm=int(lcm)
		ans.append(str(gcd)+" "+str(lcm))
	except:
		break

for i in ans:
	print(i)