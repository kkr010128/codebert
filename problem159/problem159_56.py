x = int(input())

taka = 100
count = 0

while taka < x:
    taka = taka * 101 // 100
    count += 1

print(count)
