# -*- coding: utf-8 -*-

while True:
    score = list(map(int, input().split()))
    
    if score[0] == -1 and score[1] == -1 and score[2] == -1:
        break
    elif -1 in (score[0], score[1]) or (score[0] + score[1]) < 30:
        print('F')
    elif (score[0] + score[1]) >= 80:
        print('A')
    elif 65 <= (score[0] + score[1]) < 80:
        print('B')
    elif 50 <= (score[0] + score[1]) < 65 or (30 <= (score[0] + score[1]) < 50 <= score[2]):
        print('C')
    elif 30 <= (score[0] + score[1]) < 50:
        print('D')

