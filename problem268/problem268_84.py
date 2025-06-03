N = int(input())
a_list = list(map(int, input().split()))
MOD = 10**9 + 7 

cnts = [0,0,0]
sames = 0
ind = -1
res = 1
for a in a_list:
    for i, cnt in enumerate(cnts):
        if cnt == a: 
            sames += 1
            ind = i
    res *= sames
    res %= MOD
    cnts[ind] += 1
    sames = 0

print(res)