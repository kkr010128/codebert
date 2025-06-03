n = int(input())
l = [0 for i in range(n)]
r = [0 for i in range(n)]


dat = []
dat2 = []
st = -1
for i in range(n):
    s = input()
    for ch in s:
        if ch == '(':
            r[i] += 1
            pass
        else:
            if r[i] > 0:
                r[i] -= 1
            else:
                l[i] += 1
            pass
    # print(i, l[i], r[i])
    if l[i] == 0:
        if st == -1 or r[st] < r[i]:
            st = i
    if r[i] >= l[i]:
        dat.append((l[i], i))
    else:
        dat2.append((r[i], i))

dat.sort()
dat2.sort(reverse=True)


if st == -1:
    print("No")
    exit()

now = r[st]
# print('now={}'.format(now))
for num, i in dat:
    if i == st:
        continue
    if now < l[i]:
        print("No")
        exit()
    now = now - l[i] + r[i]

for num, i in dat2:
    # print('dat2', num, i)
    if now < l[i]:
        print("No")
        exit()
    now = now - l[i] + r[i]
if now == 0:
    print("Yes")
else:
    print("No")