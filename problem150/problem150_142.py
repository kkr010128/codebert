n, k = map(int,input().split())
a = list(map(int, input().split()))
dst = [1] #今まで行った町（最初も含む）のリスト
dsts = set(dst) #今まで行った町（最初も含む）のset
twn = 1 #テレポーター転送先
for _ in range(k):
    if a[twn - 1] in dsts: #テレポーター転送先が今まで行った町setに入っていたら（そこから先の転送はループする）
        index = dst.index(a[twn - 1]) #今まで行った町リストでのテレポーター転送先のindex取得
        ld = len(dst[:index]) #ループする前の長さとループ部分の周期を求める
        cyc = len(dst[index:])
        print(dst[(ld - 1) + (k + 1 - ld) % cyc] if (k + 1 - ld) % cyc != 0 else dst[-1])
        exit()
    else: #テレポーター転送先が今まで行った町setに入っていなかったら
        dst.append(a[twn - 1]) #入っていなかったら今まで行った町リストに追加
        dsts.add(a[twn - 1])
        twn = a[twn - 1] #テレポーター転送先の更新
print(dst[-1])