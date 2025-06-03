a=100000
for _ in range(int(input())):
	a=((a*1.05)//1000+1)*1000 if (a*1.05)%1000 else a*1.05
print(int(a))