n = int(input())

if n%2 == 1:
    print(0)
    exit()

point = 0
now = 10

while now <= n:
    point += n//now
    now *= 5

print(point)