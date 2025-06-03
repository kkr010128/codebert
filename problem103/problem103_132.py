N = int(input())
A_list = [int(i) for i in input().split()]

monney = 1000
stock = 0


def max_day(index):
    if index == N-1 or (A_list[index] > A_list[index+1]):
        return index
    return max_day(index+1)


def min_day(index):
    if index == N-1:
        return -1
    if A_list[index] < A_list[index+1]:
        return index
    return min_day(index+1)


def main(day=0, flag="buy"):
    global monney, stock
    if flag == "buy":
        buy_day = min_day(day)
        if buy_day == -1:
            return monney
        stock, monney = divmod(monney, A_list[buy_day])
        return main(buy_day+1, "sell")
    elif flag == "sell":
        sell_day = max_day(day)
        monney += stock * A_list[sell_day]
        stock = 0
        if sell_day == N-1:
            return monney
        return main(sell_day+1, "buy")


print(main())
