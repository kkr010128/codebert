N = int(input())

max = 10**6

sum = 0
for i in range(1,N+1):
    if i % 3 != 0 and i % 5 != 0:
        sum = sum + i

print(sum)
