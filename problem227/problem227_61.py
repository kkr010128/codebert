number = list(map(int,input().split()))
score = list(map(int,input().split()))
score.sort()
answer = 0
if number[1] > number [0]:
    number[1] = number[0]
for i in range(number[1]):
    score[number[0]-1-i] = 0
for j in range(number[0]):
    answer += score[j]
print(answer)