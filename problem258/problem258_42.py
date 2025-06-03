n = int(input())
if n % 2 == 1:
    print(0)
    exit()

cnt = 0
x = 1
while n > 5**x:
    cnt += n//5**x//2
    x += 1
print(cnt) 