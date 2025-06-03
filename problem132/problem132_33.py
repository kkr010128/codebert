N, K = map(int, input().split())
A_list = list(map(int, input().split()))
for _ in range(K):
    count_list = [0] * N
    for i, v in enumerate(A_list):
        count_list[i - v if i - v > 0 else 0] += 1
        if i + v + 1 < N:
            count_list[i + v + 1] -= 1
    temp = 0
    flag = True
    for i in range(len(A_list)):
        temp += count_list[i]
        if temp != N:
            flag = False
        A_list[i] = temp
    if flag:
        break

print(*A_list)