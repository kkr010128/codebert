a, b, m = map(int, input().split())
a_list = [int(i) for i in input().split()]
b_list = [int(i) for i in input().split()]
money = []

for _ in range(m):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    total = a_list[x] +b_list[y] - c
    money.append(total)
money.append(min(a_list) + min(b_list))
print(min(money))