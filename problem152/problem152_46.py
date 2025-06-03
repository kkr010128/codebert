n=int(input())
lipp = []
lipm = []
limm = []
allcnt = 0
for _ in range(n):
    s = input()
    cnt = 0
    mi = 0
    for x in s:
        cnt += 1 if x == '(' else -1
        mi = min(mi,cnt)

    if cnt >= 0:
        lipm.append([mi,cnt])
    else:
        limm.append([mi - cnt, -cnt])
    allcnt += cnt
if allcnt != 0:
    print('No')
    exit()

lipm.sort(reverse = True)
limm.sort(reverse = True)

def solve(l):
    now = 0
    for mi, cnt in l:
        if mi + now < 0:
            print('No')
            exit()
        now += cnt

solve(lipm)
solve(limm)

print("Yes")