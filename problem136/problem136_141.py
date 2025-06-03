N = int(input())
dp = [True] * 10**6
count = 0
if N % 2 == 0:
    times = 0
    while(N % 2 == 0):
        times += 1
        N //= 2
    i = 1
    while(times-i >= 0):
        times -= i
        i += 1
        count += 1
f = 3
while f**2 < N:
    if N % f == 0:
        times = 0
        while(N % f == 0):
            times += 1
            N //= f
        i = 1
        while(times-i >= 0):
            times -= i
            i += 1
            count += 1
    else:
        f += 2
if N != 1:
    count += 1
print(count)