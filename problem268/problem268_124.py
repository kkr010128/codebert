N = int(input())
A = list(map(int, input().split()))
MOD = 1000000007
cnt = [0,0,0] # 現在割り当てられている人数
ans = 1 # 現時点での組み合わせ
for a in A:
    idx = []
    for i in range(3):
        if cnt[i] == a: # 割り当て可能
            idx.append(i)
    if len(idx)==0: # 割り当て不能
        print(0)
        exit()
    cnt[idx[0]]+=1 # 任意の色で良いので、一番番号が若い色とする
    ans *= len(idx) # 割り当て可能な人数をかける
    ans %= MOD
print (ans)