cards = list()
pattern = ["S", "H", "C","D"]
n = int(input())
for i in range(n) :
  s, r = input().split()  #文字列として読み込み
  r = int(r)  #sは文字列、rは数値
  if(s == "S") :
    cards.append(0 + r)
  elif(s == "H") :
    cards.append(13 + r)
  elif(s == "C") :
    cards.append(26 + r)
  else :
    cards.append(39 + r)
for i in range(1, 53) :
  if not(i in cards) :
    print(pattern[(i - 1) // 13], (i - 1) % 13 + 1)
  
