n = int(input())
x = list(map(int,input().split()))

avg1 = sum(x)//n
avg2 = avg1+1

ans1 = int(sum([(i - avg1)**2 for i in x]))
ans2 = int(sum([(i - avg2)**2 for i in x]))

print(min(ans1,ans2))
