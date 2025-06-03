from collections import deque
import numpy

N, M, X = [int(x) for x in input().split()]

stack = deque()
stack.appendleft((numpy.array([0] * M, dtype='int64'), 0, 0))

min_cost = 10**9

book_list = {}

while stack:
    info = stack.popleft()
    skill = info[0]
    cost = info[1]
    book_idx = info[2]

    if book_idx < N:
        if book_idx in book_list:
            book = book_list[book_idx]
        else:
            book = numpy.array([int(x)
                                for x in input().split()], dtype='int64')
            book_list[book_idx] = book

        after_skill = skill + book[1:]
        after_cost = cost+book[0]

        stack.appendleft((after_skill, after_cost, book_idx+1))
        stack.appendleft((skill, cost, book_idx+1))

    else:
        if cost < min_cost:
            if numpy.all(skill >= X):
                min_cost = cost

if min_cost == 10**9:
    print(-1)
else:
    print(min_cost)
