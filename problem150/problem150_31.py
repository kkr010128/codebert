N,K=map(int, input().split())
a_ls=list(map(int, input().split()))

j=1
step=0
s=set([])
l=[]
loop_s=-1
loop_g=-1

while True:
	s.add(j)
	l+=[j]
	j=a_ls[j-1] #update
	if j in s:
		loop_s=l.index(j)
		loop_g=len(l)
		break


#print(l)
#print(loop_s)
#print(loop_g)

if K<loop_s:
	print(l[K])
elif (K+1-loop_s)%(loop_g-loop_s)!=0:
	print(l[loop_s+(K+1-loop_s)%(loop_g-loop_s)-1])
else:
	print(l[-1])

