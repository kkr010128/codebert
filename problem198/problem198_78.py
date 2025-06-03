N = int(input())
# 最後の数字+1以下じゃないとだめ
# abc -> 次はa,b,c,d

dic = ["a","b","c","d","e","f","g","h","i","j"]

strs = ["a"]
cnt = 1
while cnt < N:
    tmps = []
    for s in strs:
        for i,d in enumerate(dic[::-1]):
            if d in s:
                ind = len(dic)-i-1
                break
        # print(s,ind,dic[i])
        for i in range(ind+2):
            tmps.append(s+dic[i])
    cnt += 1
    strs = tmps[:]
for s in strs:
    print(s)