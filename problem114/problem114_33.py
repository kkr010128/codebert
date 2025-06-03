def resolve():
	D = int(input())
	# 各コンテストタイプの満足度の下がりやすさ
	c = list(map(int, input().split()))
	# 各日程に各コンテストを開催した時の満足度増加量
	s = []
	for i in range(D):
		s.append(list(map(int, input().split())))
	# 最後に各コンテストを開催した日
	l = [-1] * 26
	# 満足度
	v = 0
	for d in range(D):
		# この日に開催されるコンテストタイプ
		t = int(input())-1
		l[t] = d
		# 増加分加算
		v += s[d][t]
		# 不満足分減算
		for i in range(26):
			v -= c[i] * (d - l[i])
		print(v)
resolve()