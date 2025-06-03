X = int(input())

rankArr=[2000,1800,1600,1400,1200,1000,800,600,400]

for i in range(1,len(rankArr)):
  if rankArr[i] <= X and X < rankArr[i-1] :
    print(i)
    exit()