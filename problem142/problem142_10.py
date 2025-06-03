# abc168_a.py
# https://atcoder.jp/contests/abc168/tasks/abc168_a

# A - ∴ (Therefore) /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点: 100点

# 問題文
# いろはちゃんは、人気の日本製ゲーム「ÅtCoder」で遊びたい猫のすぬけ君のために日本語を教えることにしました。
# 日本語で鉛筆を数えるときには、助数詞として数の後ろに「本」がつきます。この助数詞はどんな数につくかで異なる読み方をします。
# 具体的には、999以下の正の整数 N について、「N本」と言うときの「本」の読みは
#     Nの 1 の位が 2,4,5,7,9のとき hon
#     Nの 1 の位が 0,1,6,8のとき pon
#     Nの 1 の位が 3のとき bon
# です。
# Nが与えられるので、「N本」と言うときの「本」の読みを出力してください。

# 制約
#     Nは 999以下の正の整数

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N

# 出力
# 答えを出力せよ。

# 入力例 1
# 16

# 出力例 1
# pon

# 16の 1 の位は 6なので、「本」の読みは pon です。

# 入力例 2
# 2

# 出力例 2
# hon

# 入力例 3
# 183

# 出力例 3
# bon


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    N = int(lines[0])
    # N, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    # values = list()
    # for i in range(N):
    #     values.append(int(lines[i]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    amari = N % 10

    result = 'hon'
    if amari == 3:
        result = 'bon'
    elif amari in [0, 1, 6, 8]:
        result = 'pon'

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
        lines_input = ['16']
        lines_export = ['pon']
    if pattern == 2:
        lines_input = ['2']
        lines_export = ['hon']
    if pattern == 3:
        lines_input = ['183']
        lines_export = ['bon']
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
