# abc157_b.py
# https://atcoder.jp/contests/abc157/tasks/abc157_b

# B - Bingo /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 3×3のサイズのビンゴカードがあります。上から i 行目、左から j 列目の数は Ai,jです。

# 続けて、 N個の数 b1,b2,⋯,bNが選ばれます。
# 選ばれた数がビンゴカードの中にあった場合、ビンゴカードのその数に印を付けます。
# N個の数字が選ばれた時点でビンゴが達成されているか、則ち、縦・横・斜めのいずれか 1 列に並んだ 3つの数の組であって、
# 全てに印の付いているものが存在するかどうかを判定してください。

# 制約
#     入力は全て整数
#     1≤Ai,j≤100
#     Ai1,j1≠Ai2,j2((i1,j1)≠(i2,j2))
#     1≤N≤10
#     1≤bi≤100
#     bi≠bj(i≠j)

# 入力
# 入力は以下の形式で標準入力から与えられる。
# A1,1 A1,2 A1,3
# A2,1 A2,2 A2,3
# A3,1 A3,2 A3,3
# N
# b1
# ⋮
# bN

# 出力
# ビンゴが達成されているならば Yes と、そうでないならば No と出力せよ。

# 入力例 1
# 84 97 66
# 79 89 11
# 61 59 7
# 7
# 89
# 7
# 87
# 79
# 24
# 84
# 30

# 出力例 1
# Yes

# A1,1,A2,1,A2,2,A3,3に印が付けられます。このとき、左上から右下にかけて斜めに 3個の印が並び、ビンゴが成立しています。

# 入力例 2
# 41 7 46
# 26 89 2
# 78 92 8
# 5
# 6
# 45
# 16
# 57
# 17

# 出力例 2
# No

# 印は 1つも付いていません。

# 入力例 3
# 60 88 34
# 92 41 43
# 65 73 48
# 10
# 60
# 43
# 88
# 11
# 48
# 73
# 65
# 41
# 92
# 34

# 出力例 3
# Yes

# 全てのマスに印が付いています。


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    N = int(lines[3])
    # N, M = list(map(int, lines[0].split()))
    values_a1 = list(map(int, lines[0].split()))
    values_a2 = list(map(int, lines[1].split()))
    values_a3 = list(map(int, lines[2].split()))
    values = list()
    for i in range(N):
        values.append(int(lines[i+4]))
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    # ビンゴしているかどうかのフラグs
    flags = [0] * 9

    for n in range(N):
        if values[n] == values_a1[0]:
            flags[0] = 1
        if values[n] == values_a1[1]:
            flags[1] = 1
        if values[n] == values_a1[2]:
            flags[2] = 1
        if values[n] == values_a2[0]:
            flags[3] = 1
        if values[n] == values_a2[1]:
            flags[4] = 1
        if values[n] == values_a2[2]:
            flags[5] = 1
        if values[n] == values_a3[0]:
            flags[6] = 1
        if values[n] == values_a3[1]:
            flags[7] = 1
        if values[n] == values_a3[2]:
            flags[8] = 1

    result = 'No'
    # 横
    if flags[0] * flags[1] * flags[2] == 1:
        result = 'Yes'
    if flags[3] * flags[4] * flags[5] == 1:
        result = 'Yes'
    if flags[6] * flags[7] * flags[8] == 1:
        result = 'Yes'
    # 縦
    if flags[0] * flags[3] * flags[6] == 1:
        result = 'Yes'
    if flags[1] * flags[4] * flags[7] == 1:
        result = 'Yes'
    if flags[2] * flags[5] * flags[8] == 1:
        result = 'Yes'
    # 斜め
    if flags[0] * flags[4] * flags[8] == 1:
        result = 'Yes'
    if flags[2] * flags[4] * flags[6] == 1:
        result = 'Yes'

    return [result]


# 引数を取得
def get_input_lines():
    lines = list()
    for _ in range(3):
        lines.append(input())
    line = input()
    N = int(line)
    lines.append(line)
    for _ in range(N):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['84 97 66', '79 89 11', '61 59 7', '7', '89', '7', '87', '79', '24', '84', '30']
        lines_export = ['Yes']
    if pattern == 2:
        lines_input = ['41 7 46', '26 89 2', '78 92 8', '5', '6', '45', '16', '57', '17']
        lines_export = ['No']
    if pattern == 3:
        lines_input = ['60 88 34', '92 41 43', '65 73 48', '10', '60', '43', '88', '11', '48', '73', '65', '41', '92', '34']
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
        lines_input = get_input_lines()
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
