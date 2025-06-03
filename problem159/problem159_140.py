n = int(input())
a = 100
time = 0
while a < n:
    a += a // 100
    time += 1
print(time)