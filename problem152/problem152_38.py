n = int(input())
li = []

for _ in range(n):
    s = input()
    count = 0
    while True:
        if count + 1 >= len(s):
            break
        if s[count] == '(' and s[count+1] == ')':
            s = s[:count] + s[count+2:]
            count = max(0, count-1)
        else:
            count += 1
    li.append(s)

li2 = []
for i in li:
    count = 0
    for j in range(len(i)):
        if i[j] == ')':
            count += 1
        else:
            break
    li2.append((count, len(i) - count))

li3 = []
li4 = []

for i in li2:
    if i[0] <= i[1]:
        li3.append(i)
    else:
        li4.append(i)

li3.sort()
li4.sort(key = lambda x: x[1], reverse = True)

now = [0,0]

for l,r in li3:
    if l == 0 and r == 0:
        pass
    elif l == 0:
        now[1] += r
    else:
        now[1] -= l
        if now[1] < 0:
            print('No')
            exit()
        now[1] += r

for l,r in li4:
    if l == 0 and r == 0:
        pass
    elif r == 0:
        now[1] -= l
        if now[1] < 0:
            print('No')
            exit()
    else:
        now[1] -= l
        if now[1] < 0:
            print('No')
            exit()
        now[1] += r

if now[0] == 0 and now[1] == 0:
    print('Yes')
else:
    print('No')
