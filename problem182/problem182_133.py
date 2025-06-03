N, K, C = list(map(int, input().split(" ")))
S = input()

F_list = []
B_list = []

f_count = 0
b_count = 0
f_rest = 0
b_rest = 0
S_len = len(S)
# o
for i in range(S_len):
    if f_count == K and b_count == K:
        break

    if f_count < K:
        if S[i] == "o" and f_rest == 0:
            f_rest += C
            f_count += 1
            F_list.append(i+1)
        else:
            if f_rest > 0:
                f_rest -= 1
    if b_count < K:
        if S[-(i+1)] == "o" and b_rest == 0:
            b_rest += C
            b_count += 1
            B_list.append(S_len-i)
        else:
            if b_rest > 0:
                b_rest -= 1

for i in range(K):
    if F_list[i] == B_list[-(i+1)]:
        print(F_list[i])
