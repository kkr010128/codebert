"TLE"

N, K = map(int, input().split())

A_list = list(map(int, input().split()))

A_dir_list = []
A_visit_list = [-1 for i in range(N)]
dir = 0

while True:
    A_dir_list.append(dir)
    A_visit_list[dir] = 1
    if A_visit_list[A_list[dir]-1] == -1: 
        dir = A_list[dir]-1
    else:
        cycle_pos = A_dir_list.index(A_list[dir]-1)
        break

if K < cycle_pos:
    print(A_dir_list[K]+1)

else:
    cnt = (K-cycle_pos)%(len(A_dir_list)-cycle_pos)
    print(A_dir_list[cnt+cycle_pos]+1)
