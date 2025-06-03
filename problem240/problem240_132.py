N, M = map(int, input().split())
# [ACしたかどうか, 初ACは何回目の提出か]
prob = [[0] * 2 for _ in range(N + 1)]
# print(prob)
ps_list = [[0, 0]]

for i in range(1, M + 1):
    p, s = input().split()
    p = int(p)
    ps_list.append([p, s])
    if s == "AC" and prob[p] == [0, 0]:
        prob[p] = [1, i]


# print(prob)
# この段階でACは数えられる
ac = 0
for item in prob:
    if item[0] == 1:
        ac += 1

penalty = 0
for i in range(1, M + 1):
    p = ps_list[i][0]
    s = ps_list[i][1]
    if s == "WA" and i < prob[p][1]:
        penalty += 1

print(ac, penalty)
