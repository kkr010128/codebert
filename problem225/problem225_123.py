score = list(map(int,input().split()))
kaisu = 1
hp = score[0]
while hp > score[1]:
    kaisu += 1
    hp -= score[1]
print(kaisu)