N = input()
n = map(int,raw_input().split(' '))
c = 0
for i in range(0,N-1):
	for j in range(1,N-i):
		if n[j-1] > n[j]:
			temp = n[j-1]
			n[j-1] = n[j]
			n[j] = temp
			c += 1
print " ".join(str(i) for i in n)
print c