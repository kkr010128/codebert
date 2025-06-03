number = int(input())
words = {}
answer = []
maxnum = 0
for i in range(number):
    word = input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
    if maxnum < words[word]:
        maxnum = words[word]
        answer.clear()
        answer.append(word)
    elif maxnum == words[word]:
        answer.append(word)
answer.sort()
for j in range(len(answer)):
    print(answer[j])