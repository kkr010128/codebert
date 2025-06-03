n = int(raw_input())
elems = map(int, raw_input().split(' '))
cumul = 0
res = 0
for j in range(len(elems)):
	res += elems[j] * cumul
	cumul += elems[j]
print res
