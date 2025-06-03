n=int(input())
ans=""

for i in range(10**5):
	tmp=(n-1)%26
	ans=chr(tmp+ord("a"))+ans
	n=(n-1)//26
	if n<=0:
		break
	

print(ans)