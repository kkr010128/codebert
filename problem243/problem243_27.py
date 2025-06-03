# -*- coding: utf-8 -*-
n = int(input())
st = []
for i in range(n):
    st.append([str(i) for i in input().split()])
x = str(input())

tmp = 0
i = 0
while True:
    if st[i][0] == x:
        tmp += int(st[i][1])
        break
    else:
        tmp += int(st[i][1])
        i += 1
sum_t = 0
for i in range(n):
    sum_t += int(st[i][1])
print(sum_t - tmp)
