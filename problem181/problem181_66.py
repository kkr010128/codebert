from collections import deque

K = int(input())

queue = deque([9, 8, 7, 6, 5, 4, 3, 2, 1])

count = 0
while queue:
    number = queue.pop()
    count += 1

    if count == K:
        print(number)
        break

    last_number = int(str(number)[-1])
    add_center = number * 10 + last_number

    if last_number > 0:
        queue.appendleft(add_center - 1)

    queue.appendleft(add_center)

    if last_number < 9:
        queue.appendleft(add_center + 1)
