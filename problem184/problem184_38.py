#文字列をリストに変換
list_coffee = list(input())

#判別
if list_coffee[2] == list_coffee[3] and list_coffee[4] == list_coffee[5]:
  text = "Yes"
else:
  text = "No"

#結果の表示
print(text)