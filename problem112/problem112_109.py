N, K = map(int, input().split())
X = list(map(int, input().split()))
MOD = 10 ** 9 + 7
 
pos = sorted(v for v in X if v >= 0)
neg = sorted(-v for v in X if v < 0)
if N == K:
    ans = 1
    for x in X:
        ans *= x
        ans %= MOD
    print(ans % MOD)
    exit()
ok = False  # True: ans>=0, False: ans<0
if pos:
    #正の数があるとき
    ok = True
else:
    #全部負-> Kが奇数なら負にならざるをえない。
    ok = (K % 2 == 0)
 
ans = 1
if ok:
    # ans >= 0
    if K % 2 == 1:
        #Kが奇数の場合初めに1つ正の数を掛けておく
        #こうすれば後に非負でも負でも2つずつのペアで
        #考えられる
        ans = ans * pos.pop() % MOD
 
    # 答えは非負になる→二つの数の積は必ず非負になる．
    cand = []
    while len(pos) >= 2:
        x = pos.pop() * pos.pop()
        cand.append(x)
 
    while len(neg) >= 2:
        x = neg.pop() * neg.pop()
        cand.append(x)
 
    cand.sort(reverse=True) # ペアの積が格納されているので必ず非負
    # ペア毎に掛けていく
    for i in range(K // 2):
        ans = ans * cand[i] % MOD
else:
    # ans <= 0
    cand = sorted(X, key=lambda x: abs(x))
    for i in range(K):
        ans = ans * cand[i] % MOD
 
print(ans)