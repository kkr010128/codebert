S = input()
num = []
pre = S[0]
cnt = 0
for s in S:
    if s == pre:
        cnt += 1
    else:
        num.append(cnt)
        pre = s
        cnt = 1
num.append(cnt)

if S[0] == '>':
    num = [1] + num
if S[-1] == '<':
    num += [1]

ans = 0
for i in range(0, len(num), 2):
    b = max(num[i], num[i+1])
    c = min(num[i], num[i+1])
    ans += (b*(b+1))//2 + ((c-1)*c)//2
print(ans)