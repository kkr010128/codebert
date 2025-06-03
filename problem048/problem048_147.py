num = int(input())

array = list(map(int, input().split()))

count = 0
max = 0
sum = 0

for i in array:
    if count == 0:
        min = i
        max = i
        count += 1
    sum = sum + i
    if i < min:
        min = i
    if max < i:
        max = i

print(min, max, sum)

