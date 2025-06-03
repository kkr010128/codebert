#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

n,m,x=input2()
CA=[]
ans=10**9

for _ in range(n):
	CA.append(input_array())

# ビット全探索
for i in range(2**n):
	bag=[]
	for j in range(n): #ビット全探索
		if (i>>j) & 1:
			bag.append(CA[j])
	enoughs=[0]*m #スキルがx以上身に付く数
	skills=[0]*m #身に付くスキルの合計
	money=0 #探索中の金額

	for b in bag:
		money+=b[0]
		for k in range(1,m+1):
			skills[k-1]+=b[k]
			if skills[k-1]>=x:
				enoughs[k-1]+=1
	if 0 not in enoughs: #スキルが充足
		if money<ans:
			ans=money #価格の更新
if ans==10**9:
	print(-1)
else:
	print(ans)