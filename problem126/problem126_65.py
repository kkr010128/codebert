x= list(map(int, input().split()))
sum = 0
for i in x:
    sum = sum + i
y = 15 - int(sum)
print(int(y))