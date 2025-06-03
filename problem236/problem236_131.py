h = int(input())
w = int(input())
n = int(input())

r = max(h,w)
count = 0
x = 0
while x < n:
    count += 1
    x += r

print(count)