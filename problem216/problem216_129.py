score = list(map(int,input().split()))
if score[0] == score[1] and score[0] != score[2]:
    print('Yes')
elif score[1] == score[2] and score[0] != score[2]:
    print('Yes')
elif score[2] == score[0] and score[1] != score[2]:
    print('Yes')
else:
    print('No')