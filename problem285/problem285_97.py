S = input()
lst = []
cnt = 0
if S[0] == '<':
    flg = 0
else:
    flg = 1
for i in range(len(S)):
    if flg == 0:
        if S[i] == '<':
            cnt += 1
        elif S[i] == '>':
            lst.append(['<',cnt])
            cnt = 1
            flg = 1
    elif flg == 1:
        if S[i] == '<':
            lst.append(['>', cnt])
            cnt = 1
            flg = 0
        elif S[i] == '>':
            cnt += 1
if flg == 0:
    lst.append(['<',cnt])
else:
    lst.append(['>', cnt])
#print(lst)

ans = 0
for i in range(1,len(lst)):
    if lst[i-1][0] == '<' and lst[i][0] == '>':
       n = max(lst[i-1][1],lst[i][1])
       n2 = min(lst[i-1][1],lst[i][1])
       ans += n * (n+1) /2
       ans += (n2-1)*n2 / 2

if lst[0][0] == '>':
    n3 = lst[0][1]
    ans += n3 * (n3 + 1) / 2
if lst[-1][0] == '<':
    n4 = lst[-1][1]
    ans += n4 * (n4+1) /2
print(int(ans))