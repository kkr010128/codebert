# A - Connection and Disconnection
def count(s, c):
	count_ = s.count(c*2)
	
	while c*3 in s:
		s = s.replace(c*3, c+'_'+c)
	
	while c*2 in s:
		s = s.replace(c*2, c+'_')
	
	return min(count_, s.count('_'))


def get_startswith(s, c):
	key = c
	
	while s.startswith(key+c):
		key += c
	
	return len(key)
	
	
def get_endswith(s, c):
	key = c
	
	while s.endswith(key+c):
		key += c
	
	return len(key)


import string

S = input()
K = int(input())

lower = string.ascii_lowercase
ans = 0

if S[0] == S[-1:]:
	start = get_startswith(S, S[0])
	end = get_endswith(S, S[0])	
	
	if start == end == len(S):
		print(len(S) * K // 2)
	else:
		ans = 0
		
		ans += start // 2
		ans += end // 2
		ans += ((start + end) // 2) * (K - 1)
		
		for c in lower:
			ans += count(S[start:len(S)-end], c) * K

		print(ans)	
else:
	for c in lower:
		ans += count(S, c)

	print(ans * K)