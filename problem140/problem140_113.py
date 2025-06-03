s = input()
p = list(s) 
if p[len(p) - 1] == "?": #最後が？だったら
  p[len(p) - 1] = "D"  # Dにする
 
for i in range(len(p) - 1):
  if p[i] == "?":         # ？だったら
    if i == 0:            # 最初の文字
      if p[i + 1] == "D" or p[i + 1] == "?": # 二番目の文字がDか？
        p[i] = "P"
      else:                                   # 二番目の文字がDか？でなかったら
        p[i] = "D"
    else:
      p[i] = "D"          # D
print("".join(p))