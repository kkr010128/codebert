N = list(map(int,input().split()))
value = list(map(int,input().split()))
sum = 0
newValue = sorted(value)
for i in range(N[1]):
    sum = sum + newValue[i]
print(sum)