import sys

input = sys.stdin.readline



S = input()
T = input()

S = S.replace('\n','')
T = T.replace('\n','')

s_list = list(S)
t_list = list(T)

itti = 0
min_count = 10**5
for i in range(len(s_list)):
    if i + len(t_list) > len(s_list):
        break
    count = 0
    for j in range(len(t_list)):
        if not s_list[i+j] == t_list[j]:
            count += 1
    min_count = min(count,min_count)

print(min_count)