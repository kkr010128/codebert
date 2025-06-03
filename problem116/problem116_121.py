s_l = list(input())
t_l = list(input())

count_difference = 0
for s, t in zip(s_l, t_l):
    if s != t:
        count_difference += 1

print(count_difference)
