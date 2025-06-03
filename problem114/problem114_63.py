'''
Introduction to Heuristics Contest
A - AtCoder Contest Scheduling
'''

def main():
    # 本番テストケースは365
    D = int(input())

    # コンテストタイプごとの満足度の下がりやすさ
    C = list(map(int, input().split()))

    # 満足度row日目にコンテストcolタイプを開催したときの満足度の増加
    S = []
    for _ in range(D):
        sday = list(map(int, input().split()))
        S.append(sday)

    ''' とりあえず順番にやってくだけ
    for i in range(D):
        tmp = i % 26 + 1
        print(tmp)
    '''

    ''' 満足度Siの最高を選ぶ、満足度低下するCは未考慮
    for i in range(D):
        high = S[i].index(max(S[i])) + 1
        print(high)
    '''

#main()

def intro_heuristics_b():
    # 本番テストケースは365
    D = int(input())

    # コンテストタイプごとの満足度の下がりやすさ
    C = list(map(int, input().split()))

    # 満足度row日目にコンテストcolタイプを開催したときの満足度の増加
    S = []
    for _ in range(D):
        sday = list(map(int, input().split()))
        S.append(sday)

    # 回答(出力)
    T = [int(input()) for _ in range(D)]

    # さいごに開催したコンテストの日付
    last = [-1] * 26

    # 満足度と不満度を計算して出力
    val = 0
    for d in range(D):
        idx = T[d] - 1
        satis = S[d][idx]
        last[idx] = d
        complain = 0
        for j in range(26):
            complain += C[j] * (d - last[j])
        val += satis - complain
        print(val)

intro_heuristics_b()

#def intro_heuristics_c():
