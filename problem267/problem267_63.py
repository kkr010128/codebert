import sys
readline = sys.stdin.readline

n = int(readline())
s = readline().rstrip()

from collections import deque
q = deque([])

ss = set(s)

for i in ss:
    q.append(["",0,str(i)])

ans = 0
while q:
    num, ind, target = q.popleft()
    #print(num, ind, target)
    while ind < len(s):
        if s[ind] == target: #s[ind]が０から9の中のどれかを見てる
            break
        ind += 1
    else:
        continue
    num += target
    if len(num) == 3:
        ans += 1
        continue
    sss = set(s[ind+1:])
    for i in sss:
        q.append([num, ind +1, str(i)]) #出現した数字に関するキューを追加（例：一回目は024）

print(ans)