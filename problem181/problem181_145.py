from collections import deque
k = int(input())

# 23から232(A),233(B),234(C)が作れる
# 20からは200(B),201(C)しか作れない
# 29からは298(A),299(B)しか作れない

queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(k):
    x = queue.popleft()
    #print(x)
# (A)の場合
    if x % 10 != 0:
        queue.append(10 * x + (x % 10) - 1)
# (B)の場合
    queue.append(10 * x + x % 10)
# (C)の場合
    if x % 10 != 9:
        queue.append(10 * x + x % 10 + 1)

print(x)
