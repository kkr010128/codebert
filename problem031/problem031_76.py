import statistics

while True:
    n = int(input())
    if n == 0:
        break
    scores = list((int(x) for x in input().split()))
    
    std = statistics.pstdev(scores)
    
    print("{0:.8f}" . format(round(std,8)))
