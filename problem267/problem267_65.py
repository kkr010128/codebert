n = int(input())
s = input()
count = 0
for i in range(0,1000):
    tmp = 0
    for nun,j in enumerate(list(str(i).zfill(3))):
        pretmp = tmp
        tmp = s[tmp:].find(j)
        if tmp < 0:
            break
        if nun == 2 and tmp >= 0:
            count +=1
        tmp = tmp + pretmp + 1
print(count)