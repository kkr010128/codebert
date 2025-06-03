
N,k = map(int,input().split())

A = [0] * N
#print(A)
#print(type(A))

for okashi_number in range(k):
	di = int(input())
	D = list(map(int,input().split()))
	for x in range(di):
		A[D[x]-1]= 1
#print(A)
count = 0
for i in range(N):
	if A[i] == 0:
		count = count + 1
print(count)