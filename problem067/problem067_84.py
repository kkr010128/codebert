n = int(input())
t_point = h_point = 0
for i in range(n):
    t_card,h_card = [x for x in input().split( )]
    if t_card > h_card:
        t_point += 3
    elif t_card < h_card:
        h_point += 3
    else:
        t_point += 1
        h_point += 1
print(t_point,h_point)


