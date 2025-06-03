x,y = map(int, input().split())
count = 0
while x > 0:
    x = x - y
    count += 1
print(count)
