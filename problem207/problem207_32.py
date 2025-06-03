a  = [list(map(int,input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

for i in b:
    for j in range(3):
        for k in range(3):
            if a[j][k] == i:
                a[j][k] = 0

a_2 = list(zip(*a))
flag_1 = sum(a[0]) == 0 or sum(a[1]) == 0 or sum(a[2]) == 0
flag_2 = sum(a_2[0]) == 0 or sum(a_2[1]) == 0 or sum(a_2[2]) == 0
flag_3 = a[0][0] + a[1][1] + a[2][2] == 0 or a[0][2] + a[1][1] + a[2][0] == 0

print(['No','Yes'][flag_1 or flag_2 or flag_3])