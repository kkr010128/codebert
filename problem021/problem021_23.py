from collections import deque
s = input()
n = len(s)
stack1 = deque()
stack2 = deque()
A = 0
a = 0
for ni in range(n):
    if s[ni] == "\\":
        stack1.append(ni)
    elif s[ni] == "/" and len(stack1) > 0 :
        tmp = stack1.pop()
        A += ni - tmp
        while True:
            if len(stack2) > 0 and stack2[-1][0] > tmp:
                a += stack2.pop()[1]
            else:
                break
        a += ni - tmp
        stack2.append([ni,a])
        a = 0
print(A)
print(len(stack2),*[i[1] for i in stack2])
