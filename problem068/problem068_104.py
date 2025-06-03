S = input()
N = int(input())
for i in range(N):
    operate = input().split()
    if operate[0] == "replace":
        n = int(operate[1])
        m = int(operate[2])+1
        left_str = S[:n]
        right_str = S[m:]
        center_str = operate[3]
        S = left_str + center_str + right_str
    elif operate[0] == "reverse":
        n = int(operate[1])
        m = int(operate[2])+1
        left_str = S[:n]
        center_str = S[n:m]
        right_str = S[m:]
        center_str = center_str[::-1]
        S = left_str + center_str + right_str
    elif operate[0] == "print":
        n = int(operate[1])
        m = int(operate[2])+1
        left_str = S[:n]
        center_str = S[n:m]
        right_str = S[m:]
        print(center_str)
