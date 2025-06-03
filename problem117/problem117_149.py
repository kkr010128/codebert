
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_rui = [0]
b_rui = [0]
counta = 0
countb = 0
for i in range(n):

    a_rui.append(a_rui[i]+a[i])
    if a_rui[i+1] <= k:
        counta = i+1

for i in range(m):
    b_rui.append(b_rui[i]+b[i])
    if b_rui[i] <= k:
        countb = i+1

# print(counta, countb)
# print(a_rui, b_rui)
ans = 0
for i in range(counta+1):
    # print("DFGHj")
    # print(i, countb)
    while a_rui[i]+b_rui[countb] > k:
        # print(a_rui[i]+b_rui[countb], i, countb)
        countb -= 1
    # print(i, countb)
    ans = max(ans, i+countb)
print(ans)

