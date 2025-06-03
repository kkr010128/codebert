# abc148_c.py
# https://atcoder.jp/contests/abc148/tasks/abc148_c

# C - Snack /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点: 300点

# 問題文
# 高橋君はパーティを企画しています。
# パーティーでは参加者に 1人 1個以上のお菓子を配る予定です。
# 高橋君は参加者の人数が A人か B人のどちらかになるだろうという予想を立てました。
# どちらの場合でも均等に配りきることができるようなお菓子の個数の最小値を求めてください。
# ただし、 1個のお菓子を分割して複数人で分けることはできないものとします。

# 制約
#     1≤A,B≤105
#     A≠B入力はすべて整数

# 入力
# 入力は以下の形式で標準入力から与えられる。
# A B

# 出力
# 参加者の人数が A人の場合でも B人の場合でも均等に配りきることができるようなお菓子の個数の最小値を出力せよ。

# 入力例 1
# 2 3

# 出力例 1
# 6

# 6個のお菓子があるとき、参加者が 2 人の場合は 3 個ずつ、 3 人の場合は 2個ずつ配ることができます。

# 入力例 2
# 123 456

# 出力例 2
# 18696

# 入力例 3
# 100000 99999

# 出力例 3
# 9999900000


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
    A, B = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    import math
    result = (A*B) / math.gcd(A, B)
    result = int(result)
    
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
        lines_input = ['2 3']
        lines_export = [6]
    if pattern == 2:
        lines_input = ['123 456']
        lines_export = [18696]
    if pattern == 3:
        lines_input = ['100000 99999']
        lines_export = [9999900000]
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
