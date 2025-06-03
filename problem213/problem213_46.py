number = int(input())
score = list(map(int,input().split()))
kiroku = 10**10
for i in range(100):
    answer = 0
    for j in range(number):
        answer += (score[j] - i-1)**2
    if answer < kiroku:
        kiroku = answer
print(kiroku)