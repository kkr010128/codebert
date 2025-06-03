#ライブラリの読み込み
import math

#入力値の格納
k,x = map(int,input().split())

#判定
if k * 500 >= x:
    text = "Yes"
else:
    text = "No"

#表示
print(text)
