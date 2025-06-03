count = 0
for _ in range(int(input())):
    n = int(input())
    if n == 2 or pow(2,n-1,n) == 1:
        count += 1
print(count)
