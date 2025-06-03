score = list(map(int,input().split()))
taka = score[0]
aoki = score[2]
while taka > 0:
    aoki -= score[1]
    if aoki <= 0:
        print('Yes')
        break
    taka -= score[3]
if aoki > 0:
    print('No')