n_turn = int(input())
t_point = h_point = 0
for i in range(n_turn):
    t_card, h_card = input().split()
    if t_card > h_card:
        t_point += 3
    elif t_card == h_card:
        t_point += 1
        h_point += 1
    else:
        h_point += 3
print("{} {}".format(t_point, h_point))