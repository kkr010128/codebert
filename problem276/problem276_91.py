from itertools import accumulate

N = int(input())
A = list([int(x) for x in input().split()])

count = 0
ironbar = list(accumulate(A))

min_value = ironbar[-1]
for i in range(N):
    bet = abs(ironbar[i] - (ironbar[-1] - ironbar[i]))

    if min_value > bet:
        min_value = bet
    else:
        print(min_value)
        exit()
