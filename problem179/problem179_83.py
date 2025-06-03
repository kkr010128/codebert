# abc161_b.py
# https://atcoder.jp/contests/abc161/tasks/abc161_b

# B - Popular Vote /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# N種類の商品に対して人気投票を行いました。商品 i は Ai票を得ています。
# この中から人気商品 M個を選びます。ただし、得票数が総投票数の 14M未満であるような商品は選べません。
# 人気商品 M個を選べるなら Yes、選べないなら No を出力してください。

# 制約
#     1≤M≤N≤100
#     1≤Ai≤1000
#     Aiは相異なる
#     入力は全て整数

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N M
# A1 ... AN

# 出力
# 人気商品 M個を選べるなら Yes、選べないなら No を出力せよ。

# 入力例 1
# 4 1
# 5 4 2 1

# 出力例 1
# Yes

# 総投票数は 12です。1 位の得票数は 5なので、これを選ぶことができます。

# 入力例 2
# 3 2
# 380 19 1

# 出力例 2
# No

# 総投票数は 400です。
# 2,3 位の得票数は総得票数の 14×2 未満なので、これらを選ぶことはできず、人気商品 2個を選べません。

# 入力例 3
# 12 3
# 4 56 78 901 2 345 67 890 123 45 6 789

# 出力例 3
# Yes


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    # N = int(lines[0])
    N, M = list(map(int, lines[0].split()))
    values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    values.sort()
    values = values[::-1]

    log(f'values[M-1]=[{values[M-1]}]')
    log(f'1/(4*M)=[{1/(4*M)}]')

    if values[M-1]/sum(values) < 1/(4*M):
        result = 'No'
    else:
        result = 'Yes'

    return [result]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['4 1', '5 4 2 1']
        lines_export = ['Yes']
    if pattern == 2:
        lines_input = ['3 2', '380 19 1']
        lines_export = ['No']
    if pattern == 3:
        lines_input = ['12 3', '4 56 78 901 2 345 67 890 123 45 6 789']
        lines_export = ['Yes']
    return lines_input, lines_export


# 動作モード判別
def get_mode():
    import sys
    args = sys.argv
    global FLAG_LOG
    if len(args) == 1:
        mode = 0
        FLAG_LOG = False
    else:
        mode = int(args[1])
        FLAG_LOG = True
    return mode


# 主処理
def main():
    import time
    started = time.time()
    mode = get_mode()
    if mode == 0:
        lines_input = get_input_lines(2)
    else:
        lines_input, lines_export = get_testdata(mode)

    lines_result = calculation(lines_input)

    for line_result in lines_result:
        print(line_result)

    # if mode > 0:
    #     print(f'lines_input=[{lines_input}]')
    #     print(f'lines_export=[{lines_export}]')
    #     print(f'lines_result=[{lines_result}]')
    #     if lines_result == lines_export:
    #         print('OK')
    #     else:
    #         print('NG')
    # finished = time.time()
    # duration = finished - started
    # print(f'duration=[{duration}]')


# 起動処理
if __name__ == '__main__':
    main()
