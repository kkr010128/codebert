# -*- coding: utf-8 -*-

#整数値龍力　複数の入力
def input_multiple_number():
    return map(int, input().split())

N_given,A_given,B_given = input_multiple_number()

cnt = 0
while True:
    if (B_given - A_given)%2 == 0:
        print(cnt + (B_given-A_given)//2)
        exit(0)
    else:
        if (N_given - B_given) > (A_given-1):
            cnt += (A_given-1)
            cnt += 1
            A_given = 1
            B_given -= cnt
        else:
            cnt += (N_given - B_given)
            cnt += 1
            B_given = N_given
            A_given += cnt


