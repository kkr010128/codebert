def popular_vote():
    # 入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 総投票数
    total_vote = sum(A)
    # 総投票数の(1/4*M)以上をカウント
    count = 0
    for i in range(N):
        if A[i] >= total_vote/(4*M):
            count += 1
    if count >= M:
        return 'Yes'
    else:
        return 'No' 

result = popular_vote()
print(result)