word = list(map(int,input().split()))
score = list(map(int,input().split()))
score.sort()
score.reverse()
gokei = 0
for i in range(word[0]):
    gokei += score[i]
if score[word[1]-1]*4*word[1] >= gokei:
    print('Yes')
else:
    print('No')