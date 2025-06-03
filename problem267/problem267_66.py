def input_li():
    return list(map(int, input().split()))


def input_int():
    return int(input())


N = input_int()
S = input()
ans = 0
for i in range(1000):
    str_i = str(i)
    s = '0' * (3 - len(str_i)) + str_i
    idx = 0
    for j in range(N):
        if S[j] == s[idx]:
            idx += 1
            if idx == 3:
                ans += 1
                break
print(ans)
