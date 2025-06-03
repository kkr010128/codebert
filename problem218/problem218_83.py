N = int(input())
D = {}
for i in range(N):
	S = input()
	M = D.get(S)
	if M == None:
		D.update([(S, 1)])
	else:
		D.update([(S, M+1)])
E = list(D.keys())
F = list(D.values())
MA = max(F)
I = [i for i,x in enumerate(F) if x == MA]
ans =[]
for i in I:
	ans.append(E[i])
ans = sorted(ans)
print('\n'.join(ans))