n = int(input())
x = list(map(int,input().split()))

m = sum(x)/len(x)
m = int(round(m))
power = sum([(i - m)**2 for i in x])
print(power)