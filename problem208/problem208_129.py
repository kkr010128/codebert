#全探索版

if __name__ == '__main__':

	#n:桁数 m:チェック数
	n,m = map(int,input().split())

	B = []
	for i in range(m):
		x,y = map(int,input().split())
		B.append([x,y])

	flg = False
	for j in range(0,1000):
		tmp = str(j).zfill(n)
		#桁数同士の比較
		#桁数が異なるなら次へ
		if len(str(j)) == len(tmp):
			#チェック開始
			flg = False
			for cmd in B:
				#桁数分ループ
				t2 = cmd[0]
				t3 = str(cmd[1])

				if tmp[t2-1] != t3:
					flg = True
					break
			if flg == False:
				print(j)
				break
	if flg == True:
		print("-1")
