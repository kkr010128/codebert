#!/usr/bin/env pytho3
n = int(input())
a = list(map(int,input().split()))
# ３種類の値をもち、自分より前に同じ色の人がa[i]となる組み合わせ
# コーナーケースとして、全部同じ色なら3通り、あとは*6したらいい
# n<=10**5
# 先頭を色１、次にa[i] == 0になった点を色2,3にしてしていい。前から埋める
# 前から見ていって、それぞれの色の今の人数をcolorとして
# color.count(a[i]) == 2　ならans *= 2, ==3 ans *= 3
# 2ケースのみRE
mod = 10**9 + 7
if a == list(range(n)): print(3)
else:
  k = 0
  ans = 6
  color = [0,0,0]
  for person in range(n):
    #print(color,person)
    bit = 0#すでにcolor == a[i]が出てきているか?
    if a[person] == 0:
      if k == 3:#REになるケース
        print(0)
        exit()
      color[k] = 1
      k += 1
      continue
    for num in range(3):
      if color[num] == a[person]:
        bit += 1
        if bit == 1:
          color[num] += 1
      if num == 2: 
        ans *= bit
        ans = ans % mod
  print(ans)
