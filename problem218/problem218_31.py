n = int(input())

dic = {}
ma = 1

for i in range(n):
    wo = input()
    if(wo in dic):
        dic[wo] += 1
        if(dic[wo] > ma):
            ma = dic[wo]
    else:
        dic.update({wo:1})


ans = []
for i in dic.keys():
    if(dic[i] == ma):
        ans.append(i)
ans.sort()
for j in ans:
    print(j)
