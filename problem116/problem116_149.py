# abc172_b.py
# https://atcoder.jp/contests/abc172/tasks/abc172_b

# B - Minor Change /
# 実行時間制限: 2 sec / メモリ制限: 1024 MB
# 配点 : 200点

# 問題文
# 文字列 S, T が与えられます。次の操作を繰り返して S を Tに変更するとき、操作回数の最小値を求めてください。

# 操作：Sの 1

# 文字を選んで別の文字に書き換える

# 制約
#     S, T は長さ 1 以上 2×10^5以下
#     S, Tは英小文字のみからなる
#     Sと Tの長さは等しい

# 入力
# 入力は以下の形式で標準入力から与えられる。

# S
# T

# 出力
# 答えを出力せよ。

# 入力例 1
# cupofcoffee
# cupofhottea

# 出力例 1
# 4

# 例えば、次のような 4回の操作で達成できます。
#     1回目：6文字目の c を h に書き換える
#     2回目：8文字目の f を t に書き換える
#     3回目：9文字目の f を t に書き換える
#     4回目：11文字目の e を a に書き換える

# 入力例 2
# abcde
# bcdea

# 出力例 2
# 5

# 入力例 3
# apple
# apple

# 出力例 3
# 0

# 1度も操作をしなくてもよいこともあります。


def calculation(lines):
    S = lines[0]
    T = lines[1]
    n_diff = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            n_diff += 1
    return [n_diff]


# 引数を取得
def get_input_lines(lines_count):
    lines = list()
    for _ in range(lines_count):
        lines.append(input())
    return lines


# テストデータ
def get_testdata(pattern):
    if pattern == 1:
        lines_input = ['cupofcoffee', 'cupofhottea']
        lines_export = [4]
    if pattern == 2:
        lines_input = ['abcde', 'bcdea']
        lines_export = [5]
    if pattern == 3:
        lines_input = ['apple', 'apple']
        lines_export = [0]
    return lines_input, lines_export


# 動作モード判別
def get_mode():
    import sys
    args = sys.argv
    if len(args) == 1:
        mode = 0
    else:
        mode = int(args[1])
    return mode


# 主処理
def main():
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


# 起動処理
if __name__ == '__main__':
    main()
