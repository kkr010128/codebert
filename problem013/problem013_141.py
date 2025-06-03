def calc_max_profit(data):
    """
    http://judge.u-aizu.ac.jp/onlinejudge/commentary.jsp?id=ALDS1_1_D
    :param data: ??????????????????
    :return:
    """
    maxv = data[1] - data[0]
    minv = data[0]
    for j in range(1, len(data)):
        maxv = max(maxv, data[j] - minv)
        minv = min(minv, data[j])
    return maxv


if __name__ == '__main__':
    # ???????????\???
    num = int(input())
    data = []
    for i in range(num):
        data.append(int(input()))
    # data = [5, 3, 1, 3, 4, 3]
    # data = [4, 3, 2]

    # ??????
    result = calc_max_profit(data)

    # ???????????????
    print('{0}'.format(result))