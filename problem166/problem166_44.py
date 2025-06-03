s = input()[::-1]

dataset = [0]*2019
dataset[0] = 1

n = 0
d = 1

for i in s:
    n += int(i) * d
    a = n % 2019
    dataset[a] += 1
    d *= 10
    d %= 2019

count = 0
for i in dataset:
    count += i * (i-1) // 2

print(count)