import sys

printf = sys.stdout.write

word = []
new_word = []
for line in sys.stdin:
    word.append((line.strip("\n")).lower())
 
for i in range(len(word)):
    new_word.append(word[i].split(" "))

ans = 0
for i in range(len(new_word)):
    for j in range(len(new_word[i])):
        if new_word[i][j].count(new_word[0][0]) > 0:
            if len(new_word[i][j]) == len(new_word[0][0]):
                ans += new_word[i][j].count(new_word[0][0])


print ans - 1