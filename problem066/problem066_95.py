import sys
printf = sys.stdout.write

ans = []
while True:
    word = list(raw_input())
    if word[0] == "-":
        break

    x = input()
    suff = []

    for i in range(x):
        suff.append(input())

    for i in range(len(suff)):
        for j in range(suff[i]):
            word.insert(int(len(word)), word[0])
            del word[0]
    ans.append(word)
    word = 0


for i in range(len(ans)):
    for j in range(len(ans[i])):
        printf(ans[i][j])
    print ""