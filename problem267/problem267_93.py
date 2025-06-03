N = int(input())
S = input()

ans = 0
for i in range(0, 1000):
    if 0 <= i and i <= 9:
        num = "00"+str(i)
    elif 10 <= i and i <= 99:
        num = "0"+str(i)
    else:
        num = str(i)

    num_pos = 0
    s_pos = 0
    while True:
        if S[s_pos] == num[num_pos]:
            num_pos += 1
            if num_pos == 3:
                ans += 1
                break
        s_pos += 1
        if s_pos == N:
            break
print(ans)
