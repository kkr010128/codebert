number = list(map(int,input().split()))
score = list(map(int,input().split()))
waza = 0
for i in range(number[1]):
    waza += score[i]
if number[0] <= waza:
    print('Yes')
else:
    print('No')