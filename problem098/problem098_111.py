N=int(input())
c=input()
right_r=0
right_w=0
left_r=0
left_w=0
for i in range(N):
	if c[i]=='R':
		right_r+=1
	else:
		right_w+=1
ans=right_r
for j in range(N):
	cnt=0
	if c[j]=='W':
		left_w+=1
		right_w-=1
	else:
		left_r+=1
		right_r-=1
	if right_r<=left_w:
		cnt+=right_r
		cnt+=left_w-right_r
	else:
		cnt+=left_w
		cnt+=right_r-left_w
	if cnt<ans:
		ans=cnt
print(ans)