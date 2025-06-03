def Rally():
    # 入力
    N = int(input())
    X = list(map(int, input().split()))
    # リストの最大値と最小値
    max_num = max(X)
    min_num = min(X)
    # Pの座標を移動させて各座標の体力消耗を調べる
    min_sum = list()
    for P in range(min_num, max_num+1):
        sum = 0
        for i in range(N):
            sum += (X[i] - P)**2
        min_sum.append(sum)
    # 戻り値
    return min(min_sum)

result = Rally()
print(result)