n, k = map(int,input().split())
r, s, p = map(int,input().split())
r_s_p_points = [r, s, p]
t = input()
my_hands = []
points = 0
r_s_p = [0, 1, 2]
t_num_list = []
for i in range(n):
    if t[i] == "r":
        t_num_list.append(0)
    elif t[i] == "s":
        t_num_list.append(1)
    else:
        t_num_list.append(2)

for i in range(k):
    if t_num_list[i] == 0:
        my_hands.append(2)
        points += p
    elif t_num_list[i] == 1:
        my_hands.append(0)
        points += r
    else:
        my_hands.append(1)
        points += s

for i in range(k, n):
    if r_s_p[(t_num_list[i] - 1) % 3] != my_hands[i - k]:
        my_hands.append(r_s_p[(t_num_list[i] - 1) % 3])
        points += r_s_p_points[r_s_p[(t_num_list[i] - 1) % 3]]
    else:
        if i + k <= n-1:
            for j in range(3):
                if j == r_s_p[(t_num_list[i] - 1) % 3]:
                    continue
                elif j == r_s_p[(t_num_list[i + k] - 1) % 3]:
                    continue
                else:
                    my_hands.append(j)
                    break
        else:
            my_hands.append(0)

print(points)
