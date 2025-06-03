n = int(input())
a = list(map(int, input().split()))
num = 0
for i in a[::2]:
    if i%2 == 1:
        num += 1
print(num)