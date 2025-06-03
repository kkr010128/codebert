# 数値で入力ではなく, 文字列で入力しlist関数を使う
k = int(input())
s = input()
n = len(s)
list_s = list(s)

# リストのスライス機能を使用
if n > k:
    tmp = list_s[0:k]
    print(''.join(tmp) + '...')
else: print(''.join(list_s))