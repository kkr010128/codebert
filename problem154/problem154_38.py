n, k = map(int, input().split())
okashi = []
for _ in range(2 * k):
    okashi.append(list(map(int, input().split())))

flag = [0] * n
for i in range(int(len(okashi) / 2)):
    i = 2 * i + 1
    for j in okashi[i]:
        flag[j-1] = 1
count = 0
for i in flag:
    if i == 0:
        count += 1

print(count)