A_list = [list(map(int, input().split())) for _ in range(3)]

N = int(input())
B_list = []

for i in range(N):
    B_temp = int(input())
    B_list.append(B_temp)

ans_list = [[0 for _ in range(3)] for i in range(3)]

for i in range(N):
    for j in range(3):
        for k in range(3):
            if B_list[i] == A_list[j][k]:
                ans_list[j][k] = 1

for i in range(3):
    ans_r_flag = 0
    ans_c_flag = 0
    for j in range(3):
        ans_r_flag += ans_list[i][j]
        ans_c_flag += ans_list[j][i]
        if ans_r_flag == 3 or ans_c_flag == 3:
            print("Yes")
            exit()
            
if ans_list[0][0] == 1 and ans_list[1][1] == 1 and ans_list[2][2] == 1:
    print("Yes")
    exit()
if ans_list[0][2] == 1 and ans_list[1][1] == 1 and ans_list[2][0] == 1:
    print("Yes")
    exit()

print("No")
