bb = []
input()
aa = [ int(i) for i in input().split()]
for kk in aa[::-1]:
	bb.append(kk)
print(' '.join(map(str, bb))) #map(func, iterable)