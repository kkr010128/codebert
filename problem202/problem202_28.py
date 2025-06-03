# abc158_b.py
# https://atcoder.jp/contests/abc158/tasks/abc158_b

# B - Count Balls /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 高橋君は青と赤の 2色のボールを持っており、これらを一列に並べようとしています。
# 初め、列にボールはありません。
# 根気のある高橋君は、次の操作を 10100回繰り返します。
#     列の末尾に、A個の青いボールを加える。その後、列の末尾に B個の赤いボールを加える。
# こうしてできる列の先頭から N個のボールのうち、青いボールの個数はいくつでしょうか。

# 制約
#     1≤N≤1018
#     A,B≥0
#     0<A+B≤1018
#     入力は全て整数である

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N A B

# 出力
# 列の先頭から N個のボールのうち、青いボールの個数を出力せよ。

# 入力例 1
# 8 3 4

# 出力例 1
# 4

# 青いボールをb、赤いボールを rで表すと、列の先頭から 8個のボールは bbbrrrrb であるので、このうち青いボールは 4個です。

# 入力例 2
# 8 0 4

# 出力例 2
# 0

# そもそも赤いボールしか並んでいません。

# 入力例 3
# 6 2 4

# 出力例 3
# 2

# bbrrrr のうち青いボールは 2個です。


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
    N, A, B = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    q, mod = divmod(N, A+B)

    result = q*A + min(mod, A)

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
        lines_input = ['8 3 4']
        lines_export = [4]
    if pattern == 2:
        lines_input = ['8 0 4']
        lines_export = [0]
    if pattern == 3:
        lines_input = ['6 2 4']
        lines_export = [2]
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
        lines_input = get_input_lines(1)
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
