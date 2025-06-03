S = input()

flag = 0
for i in range(0, len(S), 1):
	if S[i] != S[len(S)-1-i]:
		flag = 1

for i in range(0, len(S)//2, 1):
	if S[i] != S[len(S)//2-1-i]:
		flag = 1

if flag == 0:
	print("Yes")
else:
	print("No")