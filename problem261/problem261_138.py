s = input()
moji = len(s)
if moji % 2 == 0:
    moji = int(moji/2)
else:
    moji = int((moji-1)/2)

answer = 0
for i in range(moji):
    if s[i] != s[len(s)-1-i]:
        answer += 1
print(answer)