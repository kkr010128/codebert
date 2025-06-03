import math

n = []
score = []
scores = []

while True:
    input_n = int(input())
    if input_n == 0:
        break
    n.append(input_n)
    input_score = [int(i) for i in input().split()]
    score.append(input_score)


def total(scorelist):
    total = 0
    for i in range(len(scorelist)):
        total = total + scorelist[i]
    return total


def ave(total,n):
    return float(total / n)

def variance(scorelist,ave,n):
    total = 0
    for i in range(len(scorelist)):
        total = total + math.pow(scorelist[i]-ave,2)
    return total / n

for i in range(len(n)):
    total_score = total(score[i])
    average = ave(total_score,n[i])
    var = variance(score[i],average,n[i])
    print(math.sqrt(var))