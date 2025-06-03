S = input()
n = len(S)+1

lr = []
num = []
a = S[0]
cnt = 0
for s in S:
    if s == a:
        cnt += 1
    else:
        num.append(cnt)
        if a == '<':
            lr.append(1)
        else:
            lr.append(0)
        a = s
        cnt = 1
num.append(cnt)
if a == '<':
    lr.append(1)
else:
    lr.append(0)

ans = 0
if (len(lr) == 1 and lr[0] == 0) or (len(lr) > 1 and lr[0] == 0):
    ans += (num[0]*(num[0]+1))//2
    lr, num = lr[1:], num[1:]
if (len(lr) == 1 and lr[0] == 1) or (len(lr) > 1 and lr[-1] == 1):
    ans += (num[-1]*(num[-1]+1))//2
    lr.pop()
    num.pop()

if not lr:
    print(ans)
    exit()

for i in range(0, len(lr), 2):
    if num[i] == num[i+1]:
        b = num[i]
        c = num[i]
    elif num[i] < num[i+1]:
        b = num[i+1]
        c = num[i]
    else:
        b = num[i]
        c = num[i+1]
    ans += (b*(b+1))//2 + ((c-1)*c)//2
print(ans)