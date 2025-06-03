import string
from itertools import zip_longest

turn = int(input())
dic = {s: i for i, s in enumerate(string.ascii_lowercase)}
t_s, h_s = 0, 0

for _ in range(turn):
    t, h = input().split()
    if t == h:
        t_s += 1
        h_s += 1
    for t_c, h_c in zip_longest(t, h, fillvalue='a'):
        if dic[t_c] > dic[h_c]:
            t_s += 3
            break
        elif dic[t_c] < dic[h_c]:
            h_s += 3
            break

print(t_s, h_s)

