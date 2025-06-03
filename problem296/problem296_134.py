S = list(input())
n = len(S)
k = int(input())
  
if len(set(S)) == 1:
  print((n * k) // 2)
  exit()

res = 0
i = 0
while i < n - 1:
  if S[i] == S[i + 1]:
    res += 1
    i += 1
  i += 1

if S[0] != S[-1]:
  print(res * k)
else:
	i = 1
	while S[0] == S[i]:
		i += 1

	j = 1
	while S[-1] == S[-1 - j]:
		j += 1
	
	if i % 2 == 0 or j % 2 == 0:
		print(res * k)
	else:
		print(res * k + (k - 1))
 