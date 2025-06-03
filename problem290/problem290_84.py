N, K = map(int, input().split())
A_list = list(map(int, input().split()))
F_list = list(map(int, input().split()))

A_list_min = sorted(A_list)
F_list_max = sorted(F_list, reverse=True)

first_OK = 10**12

def is_ok(arg):
    check_cnt = 0
    return_flag = 0
    for i in range(N):
        temp = A_list_min[i] - arg//F_list_max[i]
        if temp > 0:
            check_cnt += A_list_min[i] - arg//F_list_max[i]
    if check_cnt <= K:
        return_flag = 1
    else:
        return_flag = 0
    return return_flag

def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(bisect(-1, first_OK))