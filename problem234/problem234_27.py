n = int(input())
dic = {}
for i in range(1,n+1):
    if str(i)[-1] == 0:
        continue
    key = str(i)[0]
    key += "+" + str(i)[-1]
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1
res = 0
for i in range(1,n+1):
    if str(i)[-1] == 0:
        continue
    key = str(i)[-1]
    key += "+" + str(i)[0]
    if key in dic:
        res += dic[key]
print(res)