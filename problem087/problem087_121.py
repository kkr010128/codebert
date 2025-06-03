#B問題

#ABSの定石使うとなぜかRE

#今回はPython解説サイト参照

#①入力を文字列で受け取る→②一文字ずつ整数に変換して、forループで回しながら足し算する

N = input()
cur = 0

for i in N:
    cur += int(i)

if cur % 9 == 0:
    print("Yes")
else:
    print("No")