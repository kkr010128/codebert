score = list(map(int,input().split()))
if score[0] < 10:
    answer = score[1] + 100*(10-score[0])
else:
    answer = score[1]
print(answer)