def dfs(G,n):

	global ptr
	
	#探索済
	seen[n] = True

	#行き
	F[n] = ptr
	ptr += 1

	for i in G[n]:
		#次に行けるかを判定
		if seen[i] == True :
			continue
		dfs(G,i)

	#帰り
	L[n] = ptr
	ptr += 1

if __name__ == '__main__':

	n = int(input())
	
	G = [[] for _ in range(n+1)] 
	F = [0 for _ in range(n+1)]
	L = [0 for _ in range(n+1)]

	#深さ優先探索
	#探索済配列
	seen = [False for _ in range(n+1)]

	for i in range(n):
		cmd = list(map(int,input().split()))
		m = cmd[1]
		if m != 0:
			for j in range(m):
				G[i+1].append(cmd[j+2])
	ptr = 1
	for i in range(1,n):
		if seen[i] == False :
			dfs(G,i)

	for i in range(1,n+1):
		print(i,F[i],L[i])


