N = int(input())

answer = 'No'

for i in range(1, 9 + 1):
    for j in range(1, 9 + 1):
        if N == i * j:
            answer = 'Yes'

print(answer)