def replacing_integer():
    # 入力
    N, K = map(int, input().split())
    # 処理
    now_num = N % K
    while True:
        if abs(now_num - K) <= now_num:
            now_num = abs(now_num - K)
        else:
            return now_num

result = replacing_integer()
print(result)