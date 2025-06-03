# abc155_c.py
# https://atcoder.jp/contests/abc155/tasks/abc155_c

# C - Poll /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点: 300点

# 問題文
# N枚の投票用紙があり、i (1≤i≤N) 枚目には文字列 Siが書かれています。
# 書かれた回数が最も多い文字列を全て、辞書順で小さい順に出力してください。

# 制約
#     1≤N≤2×105
#     Siは英小文字のみからなる文字列 (1≤i≤N)
#     Siの長さは 1 以上 10 以下 (1≤i≤N)

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N
# S1
# :
# SN

# 出力
# あてはまる文字列を全て辞書順で小さい順に、改行区切りで出力せよ。

# 入力例 1
# 7
# beat
# vet
# beet
# bed
# vet
# bet
# beet

# 出力例 1
# beet
# vet

# 書かれた回数は beet と vet が 2回、beat と bed と bet が 1 回です。したがって、2回書かれた beet と vet を出力します。

# 入力例 2
# 8
# buffalo
# buffalo
# buffalo
# buffalo
# buffalo
# buffalo
# buffalo
# buffalo

# 出力例 2
# buffalo

# 入力例 3
# 7
# bass
# bass
# kick
# kick
# bass
# kick
# kick

# 出力例 3
# kick

# 入力例 4
# 4
# ushi
# tapu
# nichia
# kun

# 出力例 4
# kun
# nichia
# tapu
# ushi


global FLAG_LOG
FLAG_LOG = False


def log(value):
    # FLAG_LOG = True
    # FLAG_LOG = False
    if FLAG_LOG:
        print(str(value))


def calculation(lines):
    # S = lines[0]
    N = int(lines[0])
    # N, M = list(map(int, lines[0].split()))
    # values = list(map(int, lines[1].split()))
    # values = list(map(int, lines[2].split()))
    values = list()
    for i in range(N):
        values.append(lines[i+1])
    # valueses = list()
    # for i in range(N):
    #     valueses.append(list(map(int, lines[i+1].split())))

    dic = dict()
    for value in values:
        if value in dic:
            dic[value] += 1
        else:
            dic[value] = 1

    tmp = list()
    for key in dic:
        tmp.append(dic[key])
    ma = max(tmp)

    results = list()
    for key in dic:
        if dic[key] == ma:
            results.append(key)

    results.sort()

    return results


# 引数を取得
def get_input_lines():
    line = input()
    N = int(line)
    lines = list()
    lines.append(line)
    for _ in range(N):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['7', 'beat', 'vet', 'beet', 'bed', 'vet', 'bet', 'beet']
        lines_export = ['beet', 'vet']
    if pattern == 2:
        lines_input = ['8', 'buffalo', 'buffalo', 'buffalo', 'buffalo', 'buffalo', 'buffalo', 'buffalo', 'buffalo']
        lines_export = ['buffalo']
    if pattern == 3:
        lines_input = ['7', 'bass', 'bass', 'kick', 'kick', 'bass', 'kick', 'kick']
        lines_export = ['kick']
    if pattern == 4:
        lines_input = ['4', 'ushi', 'tapu', 'nichia', 'kun']
        lines_export = ['kun', 'nichia', 'tapu', 'ushi']
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
