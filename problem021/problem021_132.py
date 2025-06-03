from collections import deque

input = input()

stack = deque()
area = deque()

for i, v in enumerate(input):
    if v == "\\":
        stack.append(i)
    elif v == "/" and stack:
        j = stack.pop()
        ans = i - j
        while area and j<area[-1][0]:
            ans += area.pop()[1]
        area.append([j, ans])

B = [len(area)]
A = [i[1] for i in area]
print(sum(A))
B.extend(A)
print(*B)
