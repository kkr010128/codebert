(n, x, t) = tuple([int(x) for x in input().split(" ")])
summ = 0
time = 0
while summ < n:
    summ += x
    time += t
print(time)