import sys

N = int(input())
List = [[-1] * N for i in range(N)]

for i in range(N):
    A = int(input())
    for j in range(A):
        x, y = map(int, input().split())
        List[i][x - 1] = y

Max = 0

for i in range(2 ** N):

    flag = True
    Sum = 0
    for j in range(N):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            for k in range(N):
                if (List[j][k] != int((i >> k) & 1)) and List[j][k] != -1:
                    flag = False
            Sum += 1

    if flag:
        #print(i,Sum)
        Max = max(Max, Sum)

print(Max)
