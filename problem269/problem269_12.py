import math
T_1, T_2 = map(int, input().split())
A_1, A_2 = map(int, input().split())
B_1, B_2 = map(int, input().split())
ans = 0
if T_1 * A_1 + T_2 * A_2 == T_1 * B_1 + T_2 * B_2:
    print("infinity")
else:
    # 速いほうをＡと仮定
    if T_1 * A_1 + T_2 * A_2 < T_1 * B_1 + T_2 * B_2:
        A_1, A_2, B_1, B_2 = B_1, B_2, A_1, A_2
    if A_1 < B_1:
        sa_12 = T_1 * A_1 + T_2 * A_2 - (T_1 * B_1 + T_2 * B_2)  # 1サイクルでできる差
        sa_1 = -T_1 * A_1 + T_1 * B_1  # T_1でできる差
        if sa_1 % sa_12 == 0:
            ans = int((sa_1 / sa_12)*2)
        else:
            kari = math.ceil(sa_1 / sa_12)
            ans = (kari-1)*2+1
    print(ans)
