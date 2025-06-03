X = int(input())
x = X%100
cnt = 0
cnt += x//5
x = x%5
cnt += x//4
x = x%4
cnt += x//3
x = x%3
cnt += x//2
x = x%2
cnt += x
X = X-X%100
if X>=100*cnt:
    print(1)
else:
    print(0)