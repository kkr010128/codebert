s = input()
t = input()
cnt = 0

word = list(s)
answer = list(t)

for i in range(len(s)):
	if word[i] != answer[i]:
		cnt+=1


print(cnt)
