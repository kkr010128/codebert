import math

N = int(input())
P = list(map(int, input().split(" ")))
Q = list(map(int, input().split(" ")))


def find_order(num_list):
    if len(num_list) == 1:
        return 0
    first = num_list[0]
    order = sorted(num_list).index(first)
    if order == 0:
        return find_order(num_list[1:])
    else:
        return order * math.factorial(len(num_list) - 1) + find_order(num_list[1:])


order_p = find_order(P)
order_q = find_order(Q)

print(abs(order_p - order_q))
