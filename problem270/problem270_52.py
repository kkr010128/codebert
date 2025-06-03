D=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
S=input()
ans=6-D.index(S)
if ans == 0:
	ans=7
print(ans)