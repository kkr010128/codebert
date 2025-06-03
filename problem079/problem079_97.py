S = int(input())
if S <= 2:
    print(0)
elif S <= 5:
    print(1)
else:
    series = [0,0,0,1,1,1]
    m = 10**9 +7
    for i in range(6,S+1):
        series.append((series[i-3] + series[i-1]) %m)
    print(series[S])