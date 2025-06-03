import sys
n = int(input())
p_t = 0
p_h = 0

for i in range(n):
	taro, hanako = input().split()
	if taro == hanako:
		p_t += 1
		p_h += 1
	else:
		l_t = list(taro)
		l_h = list(hanako)
		for j in range(min(len(l_t), len(l_h))):
			if l_t[j] != l_h[j]:
				if ord(l_t[j])<ord(l_h[j]):
					p_h += 3
					#print('taro')
					break
				else:
					p_t += 3
					#print('hanako')
					break
			else:
				if j == min(len(l_t), len(l_h))-1:
					if len(l_t)>len(l_h):
						p_t += 3
					else:
						p_h += 3
					

print(p_t, p_h)