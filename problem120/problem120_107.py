N = list(map(int, input().split()))
fruits = list(map(int, input().split()))
sum = 0
fruits.sort()

for i in range(N[1]):
    sum +=  fruits[i]
print(sum)
