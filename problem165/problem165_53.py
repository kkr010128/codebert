scnum = int(input())
word = [0]*scnum
for i in range(scnum):
    word[i] = input()
word.sort()
answer = 1

for j in range(scnum-1):
    if word[j] != word[j+1]:
        answer += 1
print(answer)