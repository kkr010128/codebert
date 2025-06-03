n = int(input())
given_a = list(map(int, input().split()))

# money = 1000
# kabu = 0

# a = []
# for kabuka in given_a:
#     if len(a) > 0 and a[-1] == kabuka:
#         continue
#     else:
#         a.append(kabuka)

# n = len(a)
# if n == 1:
#     print(money)
#     exit()

# for i in range(n):
#     if i == 0:
#         if a[i+1] < a[i]:
#             continue
#         else:
#             kabu += money // a[i]
#             money %= a[i]
#     elif i == n-1:
#         money += kabu * a[i]
#         kabu = 0
#     else:
#         if a[i-1] < a[i] and a[i] > a[i+1]:
#             money += kabu * a[i]
#             kabu = 0
#         if a[i-1] > a[i] and a[i] < a[i+1]:
#             kabu += money // a[i]
#             money %= a[i]
# print(money)

money = 1000
kabu = 0
a = []
for kabuka in given_a:
    if len(a) > 0 and a[-1] == kabuka:
        continue
    else:
        a.append(kabuka)

n = len(a)
if n ==1:
    print(money)
    exit()

for i in range(n):
    if i == 0:
        if a[i+1] < a[i]:
            continue
        else:
            kabu += money // a[i]
            money %= a[i]
    elif i == n-1: #最後の日のとき
        money += kabu * a[i]
        kabu = 0
    else:
        if a[i-1] < a[i] and a[i] > a[i+1]:
            money += kabu * a[i]
            kabu = 0
        if a[i-1] > a[i] and a[i] < a[i+1]:
            kabu += money // a[i]
            money %= a[i]

print(money)

