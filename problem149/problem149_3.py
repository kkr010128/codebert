N, M, X = list(map(int, input().split()))

list = [list(map(int, input().split())) for i in range(N)]


def calc_cost(li):
    """
    与えられた部分リストが各アルゴリズムの条件を
    満たすか確認し、そのコストを計算。
    条件満たさないときは100000000を出力
    """

    # flag = True
    cost = 0
    for item in li:
        cost += item[0]

    for i in range(M):
        algo_sum = 0
        for item in li:
            algo_sum += item[i + 1]
        if algo_sum < X:
            return 100000000

    return cost


cost = 100000000
for i in range(2 ** N):
    in_list = []
    for j in range(N):
        if (i >> j) & 1:
            in_list.append(list[j])

    temp_cost = calc_cost(in_list)
    if temp_cost == -1:
        break
    cost = min(cost, temp_cost)

if cost == 100000000:
    cost = -1

print(cost)
