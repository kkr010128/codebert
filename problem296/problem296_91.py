s = input()
k = int(input())
s_list = []
ans = 0

def rle(s):
    tmp, count = s[0], 1
    for i in range(1, len(s)):
        if tmp == s[i]:
            count += 1
        else:
            s_list.append(count)
            tmp = s[i]
            count = 1
    s_list.append(count)
    return

rle(s)

if len(s_list) >= 2:
    for i in range(len(s_list)):
        if s_list[i] >= 2:
            ans += s_list[i] // 2

    ans *= k

    if (s_list[0] + s_list[-1]) % 2 == 0 and s[0] == s[-1]:
        ans += k - 1

else:
    ans = len(s) * k // 2

print(ans)
