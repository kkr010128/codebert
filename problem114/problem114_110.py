D = int(input())
c_list = list(map(int, input().split()))
s_list, t_list = [], []
for i in range(D):
    s_list.append(list(map(int, input().split())))

for i in range(D):
    t_list.append(int(input()))

base = 1000000
S = 0

contests_held_day = []
for i in range(26):
    contests_held_day.append(0)

for i in range(D):
    S += s_list[i][t_list[i]-1]
    contests_held_day[t_list[i]-1] = i + 1
    for j in range(26):
        S -= c_list[j] * ((i+1) - contests_held_day[j])
    print(S)
