answer = [True] * 3

a = int(input())
b = int(input())

answer[a - 1] = False
answer[b - 1] = False

for i, ans in enumerate(answer):
    if ans:
        print(i + 1)