h = int(input())
w = int(input())
n = int(input())
for i in range(min(h,w)):
    n = n - max(h,w)
    if n <= 0:
        print(i + 1)
        break