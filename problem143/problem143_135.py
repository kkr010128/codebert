# 168_b
K = int(input())
S = input()
# str.islower()
# >文字列中の大小文字の区別のある文字全てが小文字で、
# >かつ大小文字の区別のある文字が 1 文字以上あるなら True を、そうでなければ False を返します。

if (1 <= K and K <= 100) and S.islower() and (1 <= len(S) and len(S) <= 100):
    if len(S)<=K:
        print(S)

    elif len(S)>K:
        print("{}...".format(S[0:K]))
