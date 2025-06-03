import statistics

while True:
    n=int(input())
    if n==0:
        break
    
    stdnt=list(map(int,input().split()))
    
    std=statistics.pstdev(stdnt)
    
    print(std)