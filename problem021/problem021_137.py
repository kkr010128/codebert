data =input()
s1 =[]
ans =[]
memo=-1
for i in range(len(data)):
	if data[i]=='\\':
		s1.append(i)
	if data[i]=='/':
		if len(s1)==0:pass
		# elif len(s1)==1:
		# 	ans.append(i-s1.pop())
		else:
			a = i-s1[-1]
			while len(ans)!=0:
				if ans[-1][1]<=s1[-1]:break
				a+=ans.pop()[0]
			ans.append([a,s1.pop()])

	# print(ans)
ans2=[int(ans[i][0]) for i in range(len(ans))]
print(sum(ans2))
print(len(ans),end='')
if len(ans):
	print('',end=' ')
print(' '.join(list(map(str,ans2))))



