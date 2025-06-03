import sys
input = sys.stdin.buffer.readline

n = int(input())
dic = {}
cdic = {}
d = 0
for i in range(1,n+1):
    matsubi = i%10
    sentou = i//(10**d)
    if sentou >= 10:
        d += 1
        sentou = i//(10**d)
    #print(sentou,matsubi)

    if sentou == matsubi:
        if sentou not in cdic:
            cdic[sentou] = 0
        cdic[sentou] += 1
        continue

    sw = False
    if sentou > matsubi:
        sentou,matsubi = matsubi,sentou
        sw = True

    if (sentou,matsubi) not in dic:
        dic[(sentou,matsubi)] = [0,0]

    if not sw:
        dic[(sentou,matsubi)][0] += 1
    else:
        dic[(sentou,matsubi)][1] += 1

ans = 0

for item in cdic:
    ans += cdic[item]*(cdic[item])

for item in dic:
    ans += dic[item][0]*dic[item][1]*2

print(ans)
