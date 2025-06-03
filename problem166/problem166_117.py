s = list(input())
sur_list = [0 for i in range(2019)]
sur = 0
keta = 1
ans = 0

s.reverse()

for i in range(len(s)):
    keta = (keta*10)%2019
    sur_list[sur] += 1
    sur = (int(s[i]) * keta + sur) % 2019
    ans += sur_list[sur]

print(ans)
