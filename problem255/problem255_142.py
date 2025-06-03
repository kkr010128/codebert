N = int(input())
i = input().split()
S = i[0]
T = i[1]

ans=S

for i in range(N):
	print(S[i], end='')
	print(T[i], end='')