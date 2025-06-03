n = int(input())
answer = 0
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        i = 0
    else:
        answer = answer + i

print(answer)

