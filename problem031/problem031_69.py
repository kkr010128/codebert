import math

while True:
    n = input()
    
    if n == "0":
        break
    else:
        score = list(map(float, input().split()))
        m = sum(score)/len(score)
        for i in range(len(score)):
            score[i] = (score[i]-m)**2
    answer = math.sqrt(sum(score)/len(score))
    print(answer)