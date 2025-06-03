n,nWorks,nSp = map(int,input().split())

s = input()

leftList = [0]*n
rightList = [0]*n

num = 0
count = 0

while num < n:
    if s[num] == "o":
        leftList[num] = 1
        count +=1
        num += 1 + nSp
    else:
        num +=1

if count > nWorks:
    exit()

num = n-1
count = 0
while num >= 0:
    if s[num] == "o":
        rightList[num] = 1
        count +=1
        num -= (1 + nSp)
    else:
        num -=1

for kk in range(n):
    if leftList[kk] and rightList[kk]:
        print(kk+1)