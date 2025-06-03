n = int(input())

numbers = [int(i) for i in input().split(" ")]

flag = 1

cnt = 0

while flag:
    flag = 0
    for j in range(n - 1, 0, -1):
        if numbers[j] < numbers[j - 1]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            flag = 1
            cnt += 1

numbers = map(str, numbers)
print(" ".join(numbers))

print(cnt)