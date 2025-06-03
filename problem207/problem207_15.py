# -*- coding:utf-8 -*-
A_Bingo = []
for i in range(3):
    A_Bingo.append(list(map(int,input().split())))

card =[]
n = int(input())
for k in range(n):
    card.append(int(input()))

r_cnt =[0,0,0]
c_cnt =[0,0,0]
rc_result = [[0,0,0],[0,0,0],[0,0,0]]

for row in range(3):
    for column in range(3):
        if A_Bingo[row][column] in card:
            r_cnt[row] += 1
            c_cnt[column] += 1
            rc_result[row][column] = 1

if 3 in r_cnt:
    print("Yes")
elif 3 in c_cnt:
    print("Yes")
elif rc_result[0][0]*rc_result[1][1]*rc_result[2][2] == 1:
    print("Yes")
elif rc_result[0][2]*rc_result[1][1]*rc_result[2][0] == 1:
    print("Yes")
else:
    print("No")
