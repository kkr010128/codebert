import statistics

N = int(input())
X = list(map(int,input().split()))
P = round( statistics.mean(X) )

ans = sum([(i-P)**2 for i in X])
print(ans)