K = int(input())

n = 7
for i in range(K):
	if n % K == 0: 
		print(i + 1)
		exit(0)
	n = (10 * n + 7) % K
    
print('-1')