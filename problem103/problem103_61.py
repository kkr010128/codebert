a=[input() for i in range(2)]
a1=int(a[0])
a2=[int(i) for i in a[1].split()]

money=1000
kabu=0

for i in range(a1-1):
	if a2[i]<a2[i+1]:
		kabu=int(money/a2[i])
		money+=kabu*(a2[i+1]-a2[i])

print(money)