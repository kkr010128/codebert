S = input()
T = input()
lens = len(S)
lent = len(T)
ans = []
for i in range(lens - lent + 1):
	ss = S[i:i+lent]
	count = 0
	for j in range(len(ss)):
		if(ss[j] != T[j]):
			count += 1
	ans.append(count)
print(min(ans))