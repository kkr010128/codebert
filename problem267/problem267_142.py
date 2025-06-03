N = int(input())
S = str(input())

import itertools
ans=0

for num in range(1000):
	num=str(num).zfill(3)
	a0=S.find(str(num[0]))
	if a0>=0:
		S1=S[(a0+1):]
		a1=S1.find(str(num[1]))
		if a1>=0:
			S2=S1[(a1+1):]
			if str(num[2]) in S2:
				ans+=1

		



print(ans)





# 2darray [[0] * 4 for i in range(3)]