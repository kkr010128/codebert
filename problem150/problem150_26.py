N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
	A[i] -= 1

judge = N*[0]
pos = 0
freq = 0

while judge[pos]==0 and K > 0:
	judge[pos] = 1
	pos = A[pos]
	K -= 1
	freq+=1

tmp = pos
pos = 0
while pos!=tmp:
	pos = A[pos]
	freq -= 1

#print(freq)
if K==0:
	print(pos+1)
else:
	K %= freq
	pos = tmp
	for i in range(K):
		pos = A[pos]
	print(pos+1)
