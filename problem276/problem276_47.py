from collections import deque

N = int(input())
A = list(map(int, input().split()))

A = deque(A)
left = 0
right = 0
while len(A) > 1:
    if (left <= right):
        left += A.popleft()
    else:
        right += A.pop()
if left < right:
    left += A.pop()
else:
    right += A.pop()

print(max(left, right) - min(left, right))
