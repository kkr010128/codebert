def isStable(inlist, outlist):
	flag = True
	for i in range(0, N):
		for j in range(i+1, N):
			for a in range(0, N):
				for b in range(a+1, N):
					if int(inlist[i][1:]) == int(inlist[j][1:]) and inlist[i] == outlist[b] and inlist[j] == outlist[a]:
						flag = False
						break
				else:
					continue
				break
			else:
				continue
			break
		else:
			continue
		break

	return(flag)
N = int(input())
A = input().split()
B = A[:]
C = A[:]

flag = 1
counter = 0
while flag:
    flag = 0
    for i in reversed(range(1,N)):
        if int(C[i][1:]) < int(C[i-1][1:]):
            C[i], C[i-1] = C[i-1], C[i]
            counter += 1
            flag = 1
print(" ".join(map(str, C)))

if(isStable(A, C)):
	print("Stable")
else:
	print("Not stable")

counter=0
for i in range(N):
	Br = B[i:]
	Brr = [int(Br[j][1:]) for j in range(N-i)]
	num = Brr.index(min(Brr)) 
	if num != 0:
		B[i], B[(i+num)] = B[(i+num)], B[i]
		counter += 1
print(" ".join(map(str,B)))
if(isStable(A, B)):
	print("Stable")
else:
	print("Not stable")