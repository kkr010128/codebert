import sys

printf = sys.stdout.write


abc = []
ans = [0 for i in range(26)]

for i in range(26):
    abc.append(str(chr(i + 97)))


word = []
for line in sys.stdin:
    word.append(line)

for i in range(len(word)):
    for j in range(len(word[i])):
        for k in range(29):
            if (k + 65) == ord(word[i][j]) or (k + 97) == ord(word[i][j]): 
                ans[k] += 1

for i in range(26):
    printf(abc[i] + " : " + str(ans[i]) + "\n")