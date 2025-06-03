words = list(map(str,input().split()))
score = list(map(int,input().split()))
word = input()
if word == words[0]:
    print(score[0]-1,score[1])
else:
    print(score[0],score[1]-1)