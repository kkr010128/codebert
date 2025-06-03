S = input()[::-1]
 
## 余りを0~2018で総数保持
counts = [0]*2019
## 0桁の余りは0
counts[0] = 1
 
num, d = 0, 1
 
for c in S:
  ## 右から~桁の数字
  num += int(c) * d
  num %= 2019
  
  ## 次の桁
  d *= 10
  d %= 2019
  
  counts[num] += 1
  
ans = 0
for cnt in counts:
  ## nC2の計算
  ans += cnt * (cnt-1) //2
  
print(ans)