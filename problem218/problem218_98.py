import collections

N = int(input())

S_list = []

for i in range(N):
    s = input()
    S_list.append(s)

c = collections.Counter(S_list)
c_max = c.most_common()
max_num = c.most_common()[0][1]
ans_list = []
ans_list.append(c.most_common()[0][0])

for i in range(1, len(c_max)):
    if c_max[i][1] != max_num:
        break
    else:
        ans_list.append(c_max[i][0])

print(*sorted(ans_list), sep='\n')
