N = int(input())

A_li = list(map(int, input().split()))

is_rising = False
money = 1000
stock = 0

for i in range(N - 1):
    if i == 0:
        if A_li[0] < A_li[1]:
            # できるだけ買う
            stock = money // A_li[0]
            money -= A_li[0] * stock
            is_rising = True
    else:
        if is_rising:
            if A_li[i] > A_li[i + 1]:
                # 全て売る
                money += A_li[i] * stock
                stock = 0
                is_rising = False
        else:
            if A_li[i] < A_li[i + 1]:
                # できるだけ買う
                stock = money // A_li[i]
                money -= A_li[i] * stock
                is_rising = True
    if i + 1 == N - 1:
        # 全て売って終了
        money += A_li[i+1] * stock
        stock = 0

print(money)
