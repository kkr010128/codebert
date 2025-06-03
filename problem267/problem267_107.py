N = int(input())
S = input()
ans = 0
for i in range(1000):
    lucky = str(i)
    if 0 <= i <= 9:
        lucky = "00" + lucky
    elif 10 <= i <= 99:
        lucky = "0" + lucky
    else:
        pass
    now = 0
    index = 0
    while index < N:
        if lucky[now] == S[index]:
            now += 1
        if now == 3:
            ans += 1
            break
        index += 1
print(ans)
