
def count(s1,s2):
	cnt = 0
	for i in range(len(s2)):
		if s1[i] != s2[i]:
			cnt += 1
	return cnt 


S1 = input()
S2 = input()

mmin = len(S2)
for i in range(len(S1)-len(S2)+1):
	k = count(S1[i:len(S2)+i],S2)
	if k < mmin:
		mmin = k

print(mmin)

