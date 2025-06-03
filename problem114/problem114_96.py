# -*- coding: utf-8 -*-
# 入力
D = int(input())

c_i = list(map(int, input().split()))

s_d_i = []
for d in range(D):
  s_d_i.append(list(map(int, input().split())))
  
last_i = []
for i in range(26):
  last_i.append(-1)
  
# tが入力の場合（Mainでは不要） 
t_d = []
for d in range(D):
  t_d.append(int(input()))
  
  
#scoring
r_sum = 0
for d in range(D):
  t = t_d[d] - 1

  #last更新
  last_i[t] = d
  
  #c
  c_sum = 0
  for i in range(26):
    c_sum += c_i[i] * (d - last_i[i])
  
  #s - c
  r_d = s_d_i[d][t] - c_sum
  r_sum += r_d
  print(r_sum)