k = int(input())
score = list(map(int,input().split()))

answer = k - (score[0] % k)
if score[0]%k == 0:
    print('OK')
elif answer + score[0] <= score[1]:
    print('OK')
else:
    print('NG')