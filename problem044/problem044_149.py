s = raw_input().rstrip().split(" ")
ans=0
for i in range(int(s[0]),int(s[1])+1):
	if int(s[2])%i==0:ans+=1
print ans