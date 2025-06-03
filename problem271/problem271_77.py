word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())
s = input()
answer = ''
for i in range(len(s)):
    iti = word.find(s[i])
    if iti + n + 1 > len(word):
        answer += word[iti+n-len(word)]
    else:
        answer += word[iti+n]
print(answer)