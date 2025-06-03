n = int(input())
s_lst = list(str(input()) for _ in range(n))
count_lst = [0, 0, 0, 0]

for i in range(n):
    consequence = s_lst[i]
    if consequence == 'AC':
        count_lst[0] += 1
    elif consequence == 'WA':
        count_lst[1] += 1
    elif consequence == 'TLE':
        count_lst[2] += 1
    else:
        count_lst[3] += 1

consequence_lst = ['AC x {}'.format(count_lst[0]), 'WA x {}'.format(count_lst[1]), 'TLE x {}'.format(count_lst[2]), 'RE x {}'.format(count_lst[3])]

for i in range(4):
    con = consequence_lst[i]
    print(con)