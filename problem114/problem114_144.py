import numpy

D = int(input())
c_list = list(map(int, input().split()))
s_list = []

for i in range(D):
    s_list.append(list(map(int, input().split())))

t_list = []
score = 0
past_list = [0] * 26

for i in range(D):
    t_list.append(int(input()) - 1)

for i in range(D):
    for j in range(26):
        if(t_list[i] == j):
            score += s_list[i][j]
            past_list[j] = i + 1
        else:
            score -= c_list[j] * (i + 1 - past_list[j])
    print(score)