import math
x=int(input())
ans=0
for i in range (1,x+1):
	for j in range(1,x+1):
		chk=math.gcd(i,j)
		for k in range (1,x+1):
			ans=ans+math.gcd(chk,k)
print(ans)