while True:
    n = int(input())
    if n==0:
        break
    score = list(map(int, input().split()))
    ave = sum(score) / n
    print((sum([(i-ave)**2 for i in score])/n)**0.5)

