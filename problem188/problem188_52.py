#141dの応用
from collections import deque

X,Y,A,B,C = map(int, input().split())
p_list = [int(e) for e in input().split()]
q_list = [int(e) for e in input().split()]
r_list = [int(e) for e in input().split()]

p_list.sort(reverse=True)
q_list.sort(reverse=True)
r_list.sort(reverse=False)

#リストから高い方のみ取り出し
red_apples = p_list[0:min(A,X)]
green_apples = q_list[0:min(B,Y)]

colorless_apples = r_list

#print("R:",red_apples)
#print("G:",green_apples)
#print("*:",colorless_apples)
#print("########################")

#不足分をまず食べておく
if len(red_apples) < X:
    shortage = X - len(red_apples)
    red_apples += colorless_apples[0:shortage]
    del colorless_apples[0:shortage]
if len(green_apples) < Y:
    shortage = Y - len(green_apples)
    green_apples += colorless_apples[0:shortage]
    del colorless_apples[0:shortage]

#print("R:",red_apples)
#print("G:",green_apples)
#print("*:",colorless_apples)
#print("##########################")

eat_apples = red_apples + green_apples
eat_apples.sort(reverse=True)

#print("E:",eat_apples)
#print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

lowest_apple = eat_apples.pop(-1)

replaced_deque = deque() #左高 右低

#replaced_deque | eat_apples | colorless_apples
#| 1 1 2 5 7 8 12 35 58 98 | 1 3 5 7 9
#3 | 1 2 5 7 8 12 35 58 98 | 3 5 7 9
#3 3 | 2 5 7 8 12 35 58 98 | 5 7 9
#3 3 5 | 5 7 8 12 35 58 98 | 7 9
#3 3 5 | 5 7 8 12 35 58 98 | 7 9
#3 5 7 | 5 7 8 12 35 58 98 | 9
#5 7 9 | 5 7 8 12 35 58 98 |

#リンゴを低い方から、残った無色に入れ替えた方がよければ入れ替えていく。入れ替える際はより低い方を選択する
for i in range(len(colorless_apples)):

    #print("eat_apples    :" ,eat_apples)
    #print("replaced_deque:" ,replaced_deque)
    #print("lowest        :" ,lowest_apple)
    #print("candidate     :" ,colorless_apples[i])
    #print("##########################")

    if colorless_apples[i] > lowest_apple:
        replaced_deque.appendleft(colorless_apples[i])

        if len(eat_apples) > 0:
            if replaced_deque[-1] < eat_apples[-1]:
                lowest_apple = replaced_deque.pop()
            else:
                lowest_apple = eat_apples.pop(-1)
        else:
            lowest_apple = replaced_deque.pop()

print(sum(eat_apples) + sum(replaced_deque) + lowest_apple)
