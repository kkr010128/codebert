score = list(map(int,input().split()))
if score[0] <= score[1]:
    print('unsafe')
else:
    print('safe')